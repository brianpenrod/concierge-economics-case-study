# Concierge Economics Case Study (Synthetic) — Unit Economics • Scenarios • Monitoring • Executive Narrative

**Purpose:** Demonstrate how I analyze a service/product business end-to-end:
**margin drivers → scenarios → monitoring → recommendation**, using shareable synthetic data.

## What’s inside (2–5 minutes)
- **Notebook 02:** Scenario Model (Base/Upside/Downside) + sensitivity (tornado)
- **Exec Memo:** 1-page recommendation with options/tradeoffs
- **Monitoring Plan:** KPI definitions, thresholds, cadence, owners
- **Data Dictionary:** clear schema for the synthetic dataset

## Key Findings (Synthetic Sample)
- Velocity Black shows higher contribution margin than Capital One Concierge (~44% vs ~38%); main driver is higher revenue per request ($15.71 vs $13.53) despite slightly higher unit costs.
- Travel requests have the highest contribution margin (~47%) but the lowest SLA (~89%); biggest opportunity is improving Travel SLA while protecting unit economics.
- Premium tier has the strongest economics and best 90-day retention (~96–98%); Standard tier retention is lower (~91%). Mix shift and tier migration are high-leverage levers.
- **Notebook 01:** Margin Waterfall + Drivers (segment/tier breakdown)
- 
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
