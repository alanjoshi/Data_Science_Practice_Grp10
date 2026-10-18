#!/usr/bin/env python3
"""Execute the checked-in notebook from code/, using this interpreter's kernel."""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import os
from pathlib import Path
import platform
import sys
import tempfile
import time
from datetime import datetime, timezone
from importlib import metadata

ROOT = Path(__file__).resolve().parents[1]
INPUTS = ("properties.csv", "ERP.csv", "annual_household_nt.csv", "cash_rates.csv", "cpi_index.csv")
PACKAGES = ("numpy", "pandas", "scipy", "scikit-learn", "xgboost", "matplotlib", "seaborn", "joblib", "ipykernel", "nbclient", "nbformat", "jupyterlab")

PREPARATION_CHECK = '''
# Verification only: the modelling and evaluation code above is unchanged.
assert len(raw_df) == len(model_df) > 0
assert model_df["property_id"].is_unique
assert train_raw["sold_date_iso"].max() < test_raw["sold_date_iso"].min()
assert not model_df[BASE_NUMERIC + ["suburb_target_enc"]].isna().any().any()
required_exports = [PROCESSED_DIR / name for name in (
    "properties_clean.csv", "annual_household_clean.csv", "erp_clean.csv",
    "cash_rate_clean.csv", "cpi_clean.csv", "merged_raw.csv")]
required_exports.append(MODEL_READY_DIR / "model_ready.csv")
for path in required_exports:
    assert path.is_file(), f"Missing export: {path}"
    assert "address" not in pd.read_csv(path, nrows=0).columns, f"Address in CSV: {path}"
verification_summary = {
    "raw_property_rows": len(properties_raw), "clean_property_rows": len(properties),
    "merged_rows": len(merged), "model_ready_rows": len(model_df),
    "train_rows": len(train_raw), "test_rows": len(test_raw),
    "coordinate_sign_repairs": n_coords_repaired, "coordinate_exclusions": n_coords_dropped,
    "annual_macro_lag_years": ANNUAL_MACRO_LAG_YEARS, "cpi_lag_quarters": CPI_LAG_QUARTERS,
    "cutoff": str(TEMPORAL_CUTOFF), "duplicate_model_property_ids": int(model_df["property_id"].duplicated().sum()),
    "required_numeric_missing_after_preparation": int(model_df[BASE_NUMERIC + ["suburb_target_enc"]].isna().sum().sum()),
    "join_coverage_pct": {c: round(float(merged[c].notna().mean() * 100), 3)
                          for c in ["erp_population", "total_gross_income", "cash_rate_target", "cpi_index", "cpi_annual_change_pct"]},
    "exports_without_address_column": [str(p.relative_to(PROJECT_DIR)) for p in required_exports],
}
'''

SMOKE_CHECK = '''
# Small API/integration check only; these are not the tuned/report models.
smoke_models = {}
for name in MODEL_NAMES:
    params = {} if name == "Linear Regression" else {"n_estimators": 20, "max_depth": 4}
    pipe, predictions = fit_predict(name, params, NUMERIC_V1, CAT_V1, train_df, test_df.iloc[:100])
    assert len(predictions) == min(100, len(test_df)) and np.isfinite(predictions).all()
    assert (predictions > 0).all()
    smoke_path = OUTPUT_DIR / "verification" / ("smoke_" + name.lower().replace(" ", "_") + ".joblib")
    smoke_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipe, smoke_path)
    loaded = joblib.load(smoke_path)
    roundtrip = loaded.predict(test_df.iloc[:100][NUMERIC_V1 + CAT_V1])
    assert np.allclose(predictions, roundtrip)
    smoke_models[name] = {"prediction_rows": len(predictions), "serialization_roundtrip": True}
verification_summary["smoke_models"] = smoke_models
'''


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("preparation", "smoke", "full"), default="preparation",
                        help="full runs all tuning, backtests and final exports; smoke uses small untuned models")
    parser.add_argument("--timeout", type=int, default=3600, help="Per-cell timeout in seconds")
    args = parser.parse_args()
    if sys.version_info[:2] != (3, 12):
        parser.error("Use Python 3.12 for the documented verification environment.")
    missing = [name for name in INPUTS if not (ROOT / "data" / "raw" / name).is_file()]
    if missing:
        parser.error("Missing data/raw/ inputs: " + ", ".join(missing))
    from nbclient import NotebookClient
    import nbformat
    from jupyter_client import KernelManager
    from jupyter_client.kernelspec import KernelSpecManager

    source = ROOT / "code" / "main.ipynb"
    notebook = nbformat.read(source, as_version=4)
    for cell in notebook.cells:
        if cell.cell_type == "code":
            ast.parse(cell.source)
            cell.outputs = []
            cell.execution_count = None
    # Select by section boundaries so inserted explanatory cells do not shift cutoffs.
    if args.mode != "full":
        stop = next(i for i, cell in enumerate(notebook.cells)
                    if cell.cell_type == "markdown" and cell.source.startswith("## 10."))
        cells = notebook.cells[:stop]
        if args.mode == "smoke":
            definitions = next(cell for cell in notebook.cells if cell.cell_type == "code"
                               and 'TARGET = "price_numeric"' in cell.source and "def make_pipeline" in cell.source)
            cells += [nbformat.v4.new_code_cell('NUMERIC_V1 = BASE_NUMERIC + ["suburb_target_enc"]\nCAT_V1 = ["suburb", "property_type_from_address"]'), definitions]
        notebook.cells = cells
    notebook.cells.append(nbformat.v4.new_code_cell(PREPARATION_CHECK))
    if args.mode == "smoke":
        notebook.cells.append(nbformat.v4.new_code_cell(SMOKE_CHECK))
    notebook.cells.append(nbformat.v4.new_code_cell('print("VERIFICATION_SUMMARY_JSON:" + json.dumps(verification_summary))'))

    output = ROOT / "data" / "output" / "verification"
    output.mkdir(parents=True, exist_ok=True)
    report = {
        "mode": args.mode, "started_utc": datetime.now(timezone.utc).isoformat(),
        "source_commit": None, "python": platform.python_version(), "platform": platform.platform(),
        "notebook_sha256": digest(source),
        "input_sha256": {name: digest(ROOT / "data" / "raw" / name) for name in INPUTS},
        "packages": {name: metadata.version(name) for name in PACKAGES},
        "scope": ("Full unchanged notebook, plus export/preparation validation." if args.mode == "full"
                  else "Data preparation and CSV validation" + ("; three small untuned model/serialization checks." if args.mode == "smoke" else ".")
                  + " Not a reproduction of tuned metrics, backtests or final model selection."),
    }
    import subprocess
    commit = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True)
    if commit.returncode == 0:
        report["source_commit"] = commit.stdout.strip()
    start = time.monotonic()
    os.environ.setdefault("MPLBACKEND", "Agg")
    os.environ.setdefault("LOKY_MAX_CPU_COUNT", "2")
    os.environ.setdefault("OMP_NUM_THREADS", "2")
    os.environ.setdefault("OPENBLAS_NUM_THREADS", "2")
    os.environ.setdefault("MPLCONFIGDIR", str(output / "matplotlib"))
    failure = None
    # A temporary kernelspec avoids registering or changing the user's Jupyter kernels.
    with tempfile.TemporaryDirectory(prefix="darwin-kernel-") as temp:
        spec_dir = Path(temp) / "darwin-verification"
        spec_dir.mkdir()
        (spec_dir / "kernel.json").write_text(json.dumps({
            "argv": [sys.executable, "-m", "ipykernel_launcher", "-f", "{connection_file}"],
            "display_name": "Darwin verification", "language": "python",
        }))
        manager = KernelManager(kernel_name="darwin-verification", kernel_spec_manager=KernelSpecManager(kernel_dirs=[temp]))
        def progress(cell, cell_index, **kwargs):
            if cell.cell_type == "code":
                print(f"Executing cell {cell_index + 1}/{len(notebook.cells)}", flush=True)
        try:
            NotebookClient(notebook, km=manager, timeout=args.timeout,
                           resources={"metadata": {"path": str(ROOT / "code")}}, on_cell_start=progress).execute()
            for cell in notebook.cells:
                for item in cell.get("outputs", []):
                    for line in item.get("text", "").splitlines():
                        if line.startswith("VERIFICATION_SUMMARY_JSON:"):
                            report["checks"] = json.loads(line.split(":", 1)[1])
            if "checks" not in report:
                raise RuntimeError("Kernel finished without verification results.")
            report["status"] = "passed"
        except Exception as exc:
            report["status"] = "failed"
            report["error"] = str(exc)
            failure = exc
        finally:
            if manager.has_kernel:
                manager.shutdown_kernel(now=True)
    report["elapsed_seconds"] = round(time.monotonic() - start, 2)
    notebook_path = output / f"{args.mode}_executed.ipynb"
    nbformat.write(notebook, notebook_path)
    report_path = output / f"{args.mode}_report.json"
    report_path.write_text(json.dumps(report, indent=2) + "\n")
    print(f"{report['status'].upper()}: {report_path}", flush=True)
    if failure:
        print(str(failure), file=sys.stderr)
        return 1
    print(json.dumps(report["checks"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
