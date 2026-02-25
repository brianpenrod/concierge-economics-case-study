# Data Dictionary (Synthetic)

## members.csv
- member_id: unique member identifier
- segment: 'VelocityBlack' or 'CapitalOneConcierge'
- tier: 'Standard' | 'Plus' | 'Premium'
- join_date: date joined
- channel: 'Direct' | 'Partner' | 'Referral'
- monthly_fee: subscription fee (USD)
- status: 'Active' | 'Churned'
- churn_date: date churned (nullable)

## concierge_transactions.csv
- txn_id: unique transaction identifier
- member_id: link to members
- date: transaction date
- request_type: 'Dining' | 'Travel' | 'Events' | 'Gifts' | 'Lifestyle'
- revenue: revenue attributed to request (USD) — e.g., commission/fee
- variable_cost: variable fulfillment cost (USD)
- partner_fee: partner/merchant fee (USD)
- sla_met: 1 if met SLA else 0
