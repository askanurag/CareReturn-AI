import pandas as pd
from .domain_contract import validate_recording
def prepare_encounters(frame):
    validate_recording(frame);out=frame.copy()
    for name in ['admission_time','discharge_time','feature_time','followup_end']:out[name]=pd.to_datetime(out[name])
    out['return_time']=pd.to_datetime(out.return_time.replace('',pd.NaT),errors='raise')
    return out
