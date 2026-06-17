#!/usr/bin/env python3
"""Run release-readiness checks for the historical analog pipeline."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]

CHECKS = [
    ("Historical analog dataset validation", "scripts/validate_historical_analog_dataset.py"),
    ("Historical similarity matrix generation", "scripts/calculate_historical_similarity.py"),
    ("Scenario query demo generation", "scripts/run_scenario_query_demo.py"),
    ("Observed pathway generation", "scripts/generate_observed_pathways.py"),
]


def run_check(label: str, script_path: str) -> bool:
    full_path = PROJECT_ROOT / script_path
    print(f"\n==> {label}", flush=True)
    print(f"Running: {sys.executable} {script_path}", flush=True)

    result = subprocess.run(
        [sys.executable, str(full_path)],
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
    print("Repository release-readiness checks", flush=True)
    print(f"Project root: {PROJECT_ROOT}", flush=True)

    completed = 0
    for label, script_path in CHECKS:
        if not run_check(label, script_path):
            print("\nFinal summary: FAILED", flush=True)
            print(f"Checks completed before failure: {completed} of {len(CHECKS)}", flush=True)
            return 1
        completed += 1

    print("\nFinal summary: PASSED", flush=True)
    print(f"Checks completed: {completed} of {len(CHECKS)}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
