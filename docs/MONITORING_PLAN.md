# Monitoring Plan — Concierge Economics

## Goal
Detect economics drift early and ensure initiatives improve **customer outcomes** and **business value**.

## KPI Targets (Synthetic Baselines + Thresholds)
- Contribution Margin % (Velocity Black): Target 44% / Alert < 42%
- Contribution Margin % (Capital One Concierge): Target 38% / Alert < 36%
- Revenue per Request: Target $14.50 / Alert < $13.80
- Variable Cost per Request: Target $7.70 / Alert > $8.20
- Travel SLA: Target 92% / Alert < 90.5%
- Overall SLA: Target 92% / Alert < 91%
- Requests per Active Member (monthly): Target 2.2 / Alert < 1.8
- 90-day Retention: Target 92.5% / Alert < 91.5%

## KPI Table
| KPI | Definition | Why it matters | Target / Threshold | Cadence | Owner | Data Source |
|---|---|---|---|---|---|---|
| Contribution Margin % (Velocity Black) | (Revenue - Variable Costs) / Revenue | Core profitability | Target: **44%** / Alert: **<42%** | Weekly | Finance S&A Lead | Transactions + Member Fees |
| Contribution Margin % (Capital One Concierge) | (Revenue - Variable Costs) / Revenue | Core profitability | Target: **38%** / Alert: **<36%** | Weekly | Finance S&A Lead | Transactions + Member Fees |
| Revenue per Request | Total request revenue / completed requests | Margin driver (pricing/partner) | Target: **$14.50** / Alert: **<$13.80** | Weekly | Product Analytics | Transaction ledger |
| Variable Cost per Request | Variable costs / completed requests | Unit cost control | Target: **$7.70** / Alert: **>$8.20** | Weekly | Ops Analytics | Fulfillment costs |
| Requests per Active Member (Monthly) | Completed requests / active members | Utilization & value | Target: **2.2** / Alert: **<1.8** | Weekly | Product Analytics | Member + transaction logs |
| Member Retention (90d) | % retained after 90 days | LTV signal | Target: **92.5%** / Alert: **<91.5%** | Monthly | Growth Analytics | Cohort retention table |
| CAC Payback (months) | CAC / monthly contribution margin per member | Growth efficiency | Target: **≤12** / Alert: **>15** | Monthly | Growth / Finance | Marketing spend + margin |
| NPS / CSAT | Customer satisfaction score | Outcome quality | Alert: **drop >5 pts MoM** | Monthly | Customer Experience | Survey platform |
| Fulfillment SLA (Overall) | % requests met within SLA | Experience health | Target: **92%** / Alert: **<91%** | Weekly | Ops | SLA tracker |
| Fulfillment SLA (Travel) | % Travel requests met within SLA | Highest-margin, highest-risk area | Target: **92%** / Alert: **<90.5%** | Weekly | Ops | SLA tracker |

## Monitoring cadence
- **Weekly:** margin, unit cost, utilization, SLA, alerts summary
- **Monthly:** retention, CAC payback, cohort health, strategic readout
- **Quarterly:** pricing/tier review, partner economics, operating model improvements

## Alert playbook
1) Confirm data integrity (sources, pipeline health, outliers)
2) Segment the issue (product, tier, channel, partner, request type)
3) Diagnose driver (volume/mix, pricing, unit cost, churn, SLA)
4) Propose countermeasure + expected impact + monitoring plan
