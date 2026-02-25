import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import os

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "synthetic")
os.makedirs(OUT_DIR, exist_ok=True)

rng = np.random.default_rng(42)

def main():
    n_members = 1800
    segments = np.array(["VelocityBlack", "CapitalOneConcierge"])
    tiers = np.array(["Standard", "Plus", "Premium"])
    channels = np.array(["Direct", "Partner", "Referral"])

    seg = rng.choice(segments, size=n_members, p=[0.45, 0.55])
    tier = np.where(seg == "VelocityBlack",
                    rng.choice(tiers, size=n_members, p=[0.35, 0.40, 0.25]),
                    rng.choice(tiers, size=n_members, p=[0.55, 0.35, 0.10]))
    channel = rng.choice(channels, size=n_members, p=[0.55, 0.30, 0.15])

    fee_map = {"Standard": 25, "Plus": 60, "Premium": 150}
    monthly_fee = pd.Series(tier).map(fee_map).astype(float)

    end = datetime.today().date()
    start = end - timedelta(days=540)
    join_days = rng.integers(0, (end - start).days, size=n_members)
    join_date = pd.to_datetime(start) + pd.to_timedelta(join_days, unit="D")  # DatetimeIndex

    churn_prob = np.where(tier == "Standard", 0.22, np.where(tier == "Plus", 0.16, 0.10))
    churn_flag = rng.random(n_members) < churn_prob
    churn_date = pd.to_datetime(end) - pd.to_timedelta(rng.integers(10, 240, size=n_members), unit="D")  # DatetimeIndex
    churn_date = churn_date.where(churn_flag, pd.NaT)
    status = np.where(churn_flag, "Churned", "Active")

    members = pd.DataFrame({
        "member_id": [f"M{100000+i}" for i in range(n_members)],
        "segment": seg,
        "tier": tier,
        "join_date": join_date.date,
        "channel": channel,
        "monthly_fee": monthly_fee,
        "status": status,
        "churn_date": churn_date.date
    })

    request_types = np.array(["Dining", "Travel", "Events", "Gifts", "Lifestyle"])
    n_txn = 24000
    member_ids = members["member_id"].to_numpy()
    txn_member = rng.choice(member_ids, size=n_txn, replace=True)

    txn_dates = pd.to_datetime(end) - pd.to_timedelta(rng.integers(0, 180, size=n_txn), unit="D")
    req_type = rng.choice(request_types, size=n_txn, p=[0.26, 0.20, 0.18, 0.16, 0.20])

    mem_lookup = members.set_index("member_id")[["segment", "tier"]]
    seg_txn = mem_lookup.loc[txn_member, "segment"].to_numpy()
    tier_txn = mem_lookup.loc[txn_member, "tier"].to_numpy()

    base_rev = np.where(req_type == "Travel", 18, np.where(req_type == "Events", 15, 10)).astype(float)
    tier_mult = np.where(tier_txn == "Premium", 1.35, np.where(tier_txn == "Plus", 1.15, 1.0))
    seg_mult = np.where(seg_txn == "VelocityBlack", 1.10, 1.00)
    revenue = rng.normal(base_rev * tier_mult * seg_mult, 2.5).clip(0, None)

    base_cost = np.where(req_type == "Travel", 9.5, np.where(req_type == "Events", 8.5, 6.0)).astype(float)
    cost_mult = np.where(tier_txn == "Premium", 1.25, np.where(tier_txn == "Plus", 1.10, 1.0))
    variable_cost = rng.normal(base_cost * cost_mult, 1.8).clip(0, None)

    partner_fee = rng.normal(0.9, 0.35, size=n_txn).clip(0, None)

    sla_base = 0.92
    sla = sla_base + np.where(tier_txn == "Premium", 0.02, 0.0) - np.where(req_type == "Travel", 0.03, 0.0)
    sla_met = (rng.random(n_txn) < sla).astype(int)

    txns = pd.DataFrame({
        "txn_id": [f"T{200000+i}" for i in range(n_txn)],
        "member_id": txn_member,
        "date": txn_dates.date,
        "request_type": req_type,
        "revenue": revenue.round(2),
        "variable_cost": variable_cost.round(2),
        "partner_fee": partner_fee.round(2),
        "sla_met": sla_met
    })

    members.to_csv(os.path.join(OUT_DIR, "members.csv"), index=False)
    txns.to_csv(os.path.join(OUT_DIR, "concierge_transactions.csv"), index=False)
    print(f"Wrote: {OUT_DIR}/members.csv and {OUT_DIR}/concierge_transactions.csv")

if __name__ == "__main__":
    main()
