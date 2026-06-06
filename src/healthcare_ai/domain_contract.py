import numpy as np
import pandas as pd
from .settings import FEATURES
COLUMNS=['patient_id','admission_time','discharge_time','feature_time','followup_end','return_time']+FEATURES
def validate_recording(frame):
    if not set(COLUMNS)<=set(frame) or len(frame)==0:raise ValueError('Missing encounter columns or empty cohort')
    if frame.patient_id.isna().any() or not np.isfinite(frame[FEATURES].to_numpy(dtype=float)).all():raise ValueError('Finite snapshots and patient identities required')
    for name in ['admission_time','discharge_time','feature_time','followup_end']:pd.to_datetime(frame[name],errors='raise')
    admission=pd.to_datetime(frame.admission_time);discharge=pd.to_datetime(frame.discharge_time);feature=pd.to_datetime(frame.feature_time)
    if (discharge<=admission).any() or (feature>discharge).any():raise ValueError('Invalid discharge or future feature time')
    return 1.
