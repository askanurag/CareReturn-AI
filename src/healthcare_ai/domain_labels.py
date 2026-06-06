import pandas as pd
def segment_label(segment,positive_fraction=.5,horizon_days=30):
    if len(segment)!=1 or horizon_days<1:raise ValueError('One encounter and positive horizon required')
    r=segment.iloc[0];discharge=pd.Timestamp(r.discharge_time);end=pd.Timestamp(r.followup_end)
    raw=r.return_time;returned=pd.to_datetime(raw,errors='raise') if pd.notna(raw) and str(raw)!='' else pd.NaT
    if pd.notna(returned) and returned<=discharge:raise ValueError('Return must follow discharge')
    observed=pd.notna(returned) and returned<=end and returned<=discharge+pd.Timedelta(days=horizon_days)
    if observed:return 1
    if end<discharge+pd.Timedelta(days=horizon_days):raise ValueError('Censored outcome cannot be labeled negative')
    return 0
