#!/usr/bin/env python3
"""Generate a local system health report for the intelligence operations layer."""

from __future__ import annotations

import csv
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATASET_PATH = PROJECT_ROOT / "data" / "historical_analog_events.csv"
QUEUE_PATH = PROJECT_ROOT / "data" / "event_review_queue.csv"
CHANGE_LOG_PATH = PROJECT_ROOT / "data" / "dataset_change_log.csv"
COVERAGE_PATH = PROJECT_ROOT / "results" / "dataset_coverage_report.json"
OUTPUT_DIR = PROJECT_ROOT / "results"
OUTPUT_PATH = OUTPUT_DIR / "system_health_report.json"

VALIDATION_SCRIPT = PROJECT_ROOT / "scripts" / "validate_historical_analog_dataset.py"

REQUIRED_DASHBOARD_FILES = [
    PROJECT_ROOT / "dashboard" / "index.html",
    PROJECT_ROOT / "dashboard" / "app.js",
    PROJECT_ROOT / "dashboard" / "styles.css",
    PROJECT_ROOT / "results" / "scenario_query_demo_results.json",
    PROJECT_ROOT / "results" / "observed_pathways.json",
    PROJECT_ROOT / "results" / "interactive_scenario_analysis.json",
    PROJECT_ROOT / "results" / "analyst_briefs.json",
    COVERAGE_PATH,
]


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def count_dataset_rows() -> int:
    return len(read_csv_rows(DATASET_PATH))


def run_validation() -> dict[str, Any]:
    if not VALIDATION_SCRIPT.exists():
        return {
            "status": "FAIL",
            "returncode": None,
            "message": f"Validation script missing: {VALIDATION_SCRIPT}",
        }

    result = subprocess.run(
        [sys.executable, str(VALIDATION_SCRIPT)],
        cwd=PROJECT_ROOT,
        check=False,
        text=True,
        capture_output=True,
    )
    return {
        "status": "PASS" if result.returncode == 0 else "FAIL",
        "returncode": result.returncode,
        "message": result.stdout.strip().splitlines()[-1] if result.stdout.strip() else result.stderr.strip(),
    }


def build_queue_status() -> dict[str, Any]:
    rows = read_csv_rows(QUEUE_PATH)
    reviewed_statuses = {"reviewed", "approved", "rejected", "complete", "completed"}
    reviewed = sum(1 for row in rows if (row.get("review_status") or "").strip().lower() in reviewed_statuses)
    pending = sum(1 for row in rows if (row.get("review_status") or "").strip().lower() not in reviewed_statuses)
    return {
        "path": str(QUEUE_PATH.relative_to(PROJECT_ROOT)),
        "status": "PASS" if QUEUE_PATH.exists() else "WARNING",
        "queue_size": len(rows),
        "reviewed_events": reviewed,
        "pending_events": pending,
    }


def build_coverage_status(dataset_size: int) -> dict[str, Any]:
    if not COVERAGE_PATH.exists():
        return {
            "path": str(COVERAGE_PATH.relative_to(PROJECT_ROOT)),
            "status": "WARNING",
            "message": "Coverage report has not been generated.",
            "dataset_size": None,
            "matches_dataset": False,
        }

    with COVERAGE_PATH.open(encoding="utf-8") as handle:
        coverage = json.load(handle)
    coverage_size = coverage.get("dataset_size")
    return {
        "path": str(COVERAGE_PATH.relative_to(PROJECT_ROOT)),
        "status": "PASS" if coverage_size == dataset_size else "WARNING",
        "message": "Coverage report loaded.",
        "dataset_size": coverage_size,
        "matches_dataset": coverage_size == dataset_size,
    }


def latest_update_date() -> str:
    rows = read_csv_rows(CHANGE_LOG_PATH)
    dates = sorted((row.get("update_date") or "").strip() for row in rows if (row.get("update_date") or "").strip())
    return dates[-1] if dates else "Not recorded"


def build_dashboard_status() -> dict[str, Any]:
    missing = [
        str(path.relative_to(PROJECT_ROOT))
        for path in REQUIRED_DASHBOARD_FILES
        if not path.exists()
    ]
    return {
        "status": "PASS" if not missing else "WARNING",
        "missing_files": missing,
        "checked_files": [str(path.relative_to(PROJECT_ROOT)) for path in REQUIRED_DASHBOARD_FILES],
    }


def build_report() -> dict[str, Any]:
    dataset_size = count_dataset_rows()
    validation = run_validation()
    queue = build_queue_status()
    coverage = build_coverage_status(dataset_size)
    dashboard = build_dashboard_status()

    component_statuses = [
        validation["status"],
        queue["status"],
        coverage["status"],
        dashboard["status"],
    ]
    if "FAIL" in component_statuses:
        overall_status = "FAIL"
    elif "WARNING" in component_statuses:
        overall_status = "WARNING"
    else:
        overall_status = "PASS"

    return {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "overall_status": overall_status,
        "dataset_status": {
            "path": str(DATASET_PATH.relative_to(PROJECT_ROOT)),
            "status": "PASS" if DATASET_PATH.exists() and dataset_size > 0 else "FAIL",
            "dataset_size": dataset_size,
            "latest_update_date": latest_update_date(),
        },
        "queue_status": queue,
        "coverage_status": coverage,
        "validation_status": validation,
        "dashboard_status": dashboard,
        "limitations_note": (
            "System health is an operational readiness summary. It does not forecast "
            "geopolitical outcomes, estimate returns, or provide investment advice."
        ),
    }


def write_report(report: dict[str, Any]) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", encoding="utf-8") as handle:
        json.dump(report, handle, indent=2)
        handle.write("\n")


def print_summary(report: dict[str, Any]) -> None:
    print("System health report")
    print(f"Overall status: {report['overall_status']}")
    print(f"Dataset size: {report['dataset_status']['dataset_size']}")
    print(f"Queue size: {report['queue_status']['queue_size']}")
    print(f"Reviewed events: {report['queue_status']['reviewed_events']}")
    print(f"Pending events: {report['queue_status']['pending_events']}")
    print(f"Coverage status: {report['coverage_status']['status']}")
    print(f"Validation status: {report['validation_status']['status']}")
    print(f"Dashboard status: {report['dashboard_status']['status']}")
    print(f"Output path: {OUTPUT_PATH}")


def main() -> int:
    try:
        report = build_report()
        write_report(report)
        print_summary(report)
        return 0 if report["overall_status"] in {"PASS", "WARNING"} else 1
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
