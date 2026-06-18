# Visual Portfolio Polish Summary

## Screenshots Added

Sprint 9 adds two dashboard screenshots under `figures/`:

- `figures/dashboard_overview.png`
- `figures/dashboard_pathways.png`

## What Each Screenshot Shows

`dashboard_overview.png` shows the top of the static dashboard evidence view, including the project title, data-loading status, dissertation theory chain, scenario questions, top historical analogues, similarity scores, observed pathways, and evidence notes.

`dashboard_pathways.png` shows the observed pathway section, including grouped historical patterns, pathway counts, representative events, analyst notes, evidence notes, and the limitations / not-investment-advice panel.

## Why This Improves Portfolio Readability

The screenshots make the repository easier to understand from the GitHub landing page. A reader can see the final evidence interface before running the local dashboard, which helps connect the dissertation research, deterministic scripts, generated JSON outputs, and dashboard presentation into one visible portfolio artefact.

The screenshots do not add new analytics functionality and do not change the project claims. They are visual documentation of the existing dashboard.

## How to Regenerate Screenshots Manually

From the repository root, run:

```bash
python3 -m http.server 8000
```

Open:

```text
http://127.0.0.1:8000/dashboard/
```

Capture:

1. the top dashboard view and save it as `figures/dashboard_overview.png`;
2. the observed pathways section and save it as `figures/dashboard_pathways.png`.

If the dashboard does not load data, first run:

```bash
python3 scripts/run_all_checks.py
```

Then reload the dashboard and recapture the screenshots.
