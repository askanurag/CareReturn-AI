import numpy as np
import pandas as pd
def make_recording(seed=1):
    rng=np.random.default_rng(seed);rows=[]
    for patient in range(20):
        age=int(rng.integers(25,85))
        for episode in range(2):
            prior=int(rng.integers(0,5));comorb=int(rng.integers(0,6));stay=int(rng.integers(1,12));meds=int(rng.integers(1,12));delay=int(rng.integers(1,22))
            admission=pd.Timestamp('2025-01-01')+pd.Timedelta(days=patient*2+episode*120);discharge=admission+pd.Timedelta(days=stay)
            probability=1/(1+np.exp(-(-3+prior*.5+comorb*.35+delay*.04)))
            outcome=bool(rng.random()<probability);return_time=discharge+pd.Timedelta(days=int(rng.integers(1,30))) if outcome else pd.NaT
            rows.append({'patient_id':'CARE-SIM-%02d-%03d'%(seed,patient),'admission_time':admission.isoformat(),'discharge_time':discharge.isoformat(),
             'feature_time':discharge.isoformat(),'followup_end':(discharge+pd.Timedelta(days=45)).isoformat(),'return_time':return_time.isoformat() if outcome else '',
             'age':age,'length_of_stay':stay,'prior_admissions':prior,'comorbidity_count':comorb,'medication_count':meds,'followup_delay':delay})
    return pd.DataFrame(rows)
