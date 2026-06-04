import pandas as pd
def admission_features(frame):
    out=frame.copy();out['medications_per_comorbidity']=out.medication_count/(1+out.comorbidity_count.clip(lower=0))
    out['prior_admissions_per_stay_day']=out.prior_admissions/out.length_of_stay.clip(lower=1)
    return out
def check_feature_availability(available_times,prediction_time):
    late=[name for name,time in available_times.items() if pd.Timestamp(time)>pd.Timestamp(prediction_time)]
    if late:raise ValueError('Unavailable at prediction time: '+str(late))
    return True
