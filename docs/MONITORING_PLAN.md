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
| Contribution Margin % | (Revenue - Variable Costs) / Revenue | Core profitability | Target: {{X}}% / Alert: <{{Y}}% | Weekly | {{Owner}} | {{Source}} |
| Variable Cost per Request | Variable costs / completed requests | Unit cost control | Alert: >{{X}} | Weekly | {{Owner}} | {{Source}} |
| Requests per Active Member | Completed requests / active members | Utilization & value | Target: {{X}} | Weekly | {{Owner}} | {{Source}} |
| Member Retention (90d) | % retained after 90 days | LTV signal | Alert: <{{X}}% | Monthly | {{Owner}} | {{Source}} |
| CAC Payback (months) | CAC / monthly contribution margin per member | Growth efficiency | Alert: >{{X}} months | Monthly | {{Owner}} | {{Source}} |
| NPS / CSAT | Customer sentiment | Outcome quality | Alert: drop >{{X}} pts | Monthly | {{Owner}} | {{Source}} |
| Fulfillment SLA | % requests met within SLA | Experience | Alert: <{{X}}% | Weekly | {{Owner}} | {{Source}} |

## Monitoring cadence
- **Weekly:** margin, unit cost, utilization, SLA, alerts summary
- **Monthly:** retention, CAC payback, cohort health, strategic readout
- **Quarterly:** pricing/tier review, partner economics, operating model improvements

## Alert playbook
1) Confirm data integrity (sources, pipeline health, outliers)
2) Segment the issue (product, tier, channel, partner, request type)
3) Diagnose driver (volume/mix, pricing, unit cost, churn, SLA)
4) Propose countermeasure + expected impact + monitoring plan
