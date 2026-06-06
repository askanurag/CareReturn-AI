from .settings import FEATURES
def segment_features(segment,fs=None):
    if len(segment)!=1:raise ValueError('One discharge snapshot required')
    return {f:float(segment[f].iloc[0]) for f in FEATURES}
