import pandas as pd

def project_monthly_economics(
    base_members: int,
    arpu_fee: float,
    requests_per_member: float,
    revenue_per_request: float,
    variable_cost_per_request: float,
    partner_fee_per_request: float,
    monthly_growth: float,
    monthly_churn: float,
    months: int = 12
):
    rows = []
    members = float(base_members)
    for m in range(1, months + 1):
        members = members * (1 + monthly_growth) * (1 - monthly_churn)
        subs_rev = members * arpu_fee
        reqs = members * requests_per_member
        txn_rev = reqs * revenue_per_request
        var_cost = reqs * variable_cost_per_request
        partner = reqs * partner_fee_per_request

        total_rev = subs_rev + txn_rev
        contribution = total_rev - var_cost - partner
        rows.append({
            "month": m,
            "members": members,
            "subscription_revenue": subs_rev,
            "transaction_revenue": txn_rev,
            "total_revenue": total_rev,
            "variable_cost": var_cost,
            "partner_fee": partner,
            "contribution": contribution,
            "contribution_margin_pct": (contribution / total_rev) if total_rev else 0.0
        })
    return pd.DataFrame(rows)
