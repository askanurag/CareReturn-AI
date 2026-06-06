import pandas as pd
from .domain_contract import validate_recording
def recording_quality(frame):
    validate_recording(frame);discharge=pd.to_datetime(frame.discharge_time);end=pd.to_datetime(frame.followup_end)
    return {'encounters':len(frame),'patients':int(frame.patient_id.nunique()),'repeat_patient_rows':int(frame.patient_id.duplicated().sum()),
      'followup_days_min':float((end-discharge).dt.total_seconds().min()/86400),'post_discharge_feature_rows':int((pd.to_datetime(frame.feature_time)>discharge).sum())}
