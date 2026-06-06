import pandas as pd
from .domain_loader import load_recording
from .domain_windows import segments
from .domain_features import segment_features
from .domain_labels import segment_label
from .settings import FEATURES,TARGET
def cohort_from_paths(paths,window_size=30,stride_size=1,noise_sigma=0.,seed=42):
    # window_size is the outcome horizon in days.
    import numpy as np
    if noise_sigma<0:raise ValueError('Nonnegative noise required')
    rng=np.random.default_rng(seed);rows=[]
    for path in paths:
        f=load_recording(path)
        for row in segments(f,window_size,stride_size):
            features=segment_features(row)
            if noise_sigma:features={k:max(0.,v+rng.normal(0,noise_sigma)) for k,v in features.items()}
            rows.append({'patient_id':row.patient_id.iloc[0],**features,TARGET:segment_label(row,horizon_days=window_size)})
    if not rows:raise ValueError('No index encounters')
    return pd.DataFrame(rows,columns=['patient_id']+FEATURES+[TARGET])
