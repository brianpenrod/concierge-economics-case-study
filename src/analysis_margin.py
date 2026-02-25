import pandas as pd

def load_data(members_path: str, txns_path: str):
    members = pd.read_csv(members_path, parse_dates=["join_date", "churn_date"])
    txns = pd.read_csv(txns_path, parse_dates=["date"])
    return members, txns

def compute_contribution_margin(members: pd.DataFrame, txns: pd.DataFrame):
    df = txns.merge(members[["member_id","segment","tier","monthly_fee","status"]], on="member_id", how="left")
    df["contrib"] = df["revenue"] - df["variable_cost"] - df["partner_fee"]
    out = (df.groupby(["segment","tier"])
             .agg(txn_count=("txn_id","count"),
                  revenue=("revenue","sum"),
                  variable_cost=("variable_cost","sum"),
                  partner_fee=("partner_fee","sum"),
                  contribution=("contrib","sum"),
                  sla_met=("sla_met","mean"))
             .reset_index())
    out["contribution_margin_pct"] = out["contribution"] / out["revenue"]
    return out
