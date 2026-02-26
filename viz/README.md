# Visualizing Concierge Economics

This directory contains key visualizations derived from the quantitative models in the `notebooks/` and `src/` directories.

## 1. Profit Distribution (Monte Carlo Simulation)
**File:** `concierge_profit_distribution.png`
* **Objective:** Illustrates annual net profit probability under stochastic conditions (volume and revenue volatility).
* **Key Metric:** Expected Value (Mean) vs. Value at Risk (VaR).
* **Insight:** Demonstrates that at a 636-request monthly volume, the business operates on a "Neutral Trend." To move to a "Positive Expectancy" model, volume must scale to 750+ or revenue must increase to $18+.

## 2. Breakeven Sensitivity Heatmap
**File:** `sensitivity_heatmap.png`
* **Objective:** Visualizes the "Profitability Floor" across varying Fixed Cost tiers and Revenue per Request.
* **Key Metric:** Breakeven Units (Monthly Requests).
* **Insight:** Highlights the "Green Zone" (Lower volume requirement) as Revenue per Request approaches the $18-$20 range. This supports **Option A** in the Executive Memo: leveraging pricing/partner terms to reduce operational strain.
