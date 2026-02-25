# Concierge Economics Case Study (Synthetic) — Unit Economics • Scenarios • Monitoring • Executive Narrative

**Purpose:** Demonstrate how I analyze a service/product business end-to-end:
**margin drivers → scenarios → monitoring → recommendation**, using shareable synthetic data.

## What’s inside (2–5 minutes)
- **Notebook 01:** Margin Waterfall + Drivers (segment/tier breakdown)
- **Notebook 02:** Scenario Model (Base/Upside/Downside) + sensitivity (tornado)
- **Exec Memo:** 1-page recommendation with options/tradeoffs
- **Monitoring Plan:** KPI definitions, thresholds, cadence, owners
- **Data Dictionary:** clear schema for the synthetic dataset

## Repository structure
```
concierge-economics-case-study/
  data/
    synthetic/
      members.csv
      concierge_transactions.csv
  docs/
    EXEC_MEMO.md
    MONITORING_PLAN.md
    DATA_DICTIONARY.md
  notebooks/
    01_margin_waterfall.ipynb
    02_scenario_model.ipynb
  src/
    generate_synthetic_data.py
    analysis_margin.py
    scenario_model.py
  requirements.txt
```

## How to run
```bash
python -m venv .venv && source .venv/bin/activate  # windows: .venv\Scripts\activate
pip install -r requirements.txt
python src/generate_synthetic_data.py
jupyter notebook
```
