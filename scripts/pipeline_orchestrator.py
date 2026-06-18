#!/usr/bin/env python3
"""Run the semi-automated intelligence pipeline in deterministic order."""

from __future__ import annotations

import csv
import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
QUEUE_PATH = PROJECT_ROOT / "data" / "event_review_queue.csv"

PIPELINE_STEPS = [
    ("Step 1", "Validate dataset", ["scripts/validate_historical_analog_dataset.py"]),
    ("Step 3", "Generate coverage analytics", ["scripts/dataset_coverage_analysis.py"]),
    ("Step 4", "Generate similarity outputs", ["scripts/calculate_historical_similarity.py"]),
    ("Step 5a", "Generate scenario query outputs", ["scripts/run_scenario_query_demo.py"]),
    ("Step 5b", "Generate interactive scenario outputs", ["scripts/analyze_scenario_profile.py"]),
    ("Step 6", "Generate pathway outputs", ["scripts/generate_observed_pathways.py"]),
    ("Step 7", "Generate analyst brief outputs", ["scripts/generate_analyst_brief.py"]),
    ("Step 8", "Generate dashboard operations data", ["scripts/system_health_report.py"]),
]


def check_review_queue() -> bool:
    print("\n==> Step 2: Check review queue", flush=True)
    if not QUEUE_PATH.exists():
        print(f"FAIL: Review queue missing: {QUEUE_PATH}", flush=True)
        return False

    with QUEUE_PATH.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    required_fields = [
        "queue_id",
        "event_title",
        "event_date",
        "source_name",
        "source_url",
        "candidate_status",
        "review_status",
        "assigned_reviewer",
        "review_date",
        "final_decision",
        "notes",
    ]
    with QUEUE_PATH.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        columns = reader.fieldnames or []
        missing = [field for field in required_fields if field not in columns]

    if missing:
        print(f"FAIL: Review queue missing required fields: {', '.join(missing)}", flush=True)
        return False

    pending = sum(1 for row in rows if (row.get("review_status") or "").strip().lower() not in {"reviewed", "approved", "rejected", "complete", "completed"})
    print(f"PASS: Review queue available ({len(rows)} candidate(s), {pending} pending)", flush=True)
    return True


def run_script(step: str, label: str, command: list[str]) -> bool:
    print(f"\n==> {step}: {label}", flush=True)
    print(f"Running: {sys.executable} {' '.join(command)}", flush=True)
    result = subprocess.run(
        [sys.executable, *command],
        cwd=PROJECT_ROOT,
        check=False,
        text=True,
    )
    if result.returncode == 0:
        print(f"PASS: {label}", flush=True)
        return True
    print(f"FAIL: {label} exited with status {result.returncode}", flush=True)
    return False


def main() -> int:
    print("Semi-automated intelligence pipeline orchestrator", flush=True)
    print(f"Project root: {PROJECT_ROOT}", flush=True)

    completed = 0
    total_steps = len(PIPELINE_STEPS) + 1

    if not run_script(*PIPELINE_STEPS[0]):
        print("\nFinal summary: FAIL", flush=True)
        print(f"Steps completed before failure: {completed} of {total_steps}", flush=True)
        return 1
    completed += 1

    if not check_review_queue():
        print("\nFinal summary: FAIL", flush=True)
        print(f"Steps completed before failure: {completed} of {total_steps}", flush=True)
        return 1
    completed += 1

    for step in PIPELINE_STEPS[1:]:
        if not run_script(*step):
            print("\nFinal summary: FAIL", flush=True)
            print(f"Steps completed before failure: {completed} of {total_steps}", flush=True)
            return 1
        completed += 1

    print("\nFinal summary: PASS", flush=True)
    print(f"Steps completed: {completed} of {total_steps}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
