import json
SPEC = json.loads('{"slug": "CareReturn_AI", "title": "CareReturn AI", "task": "Synthetic hospital readmission classification", "features": ["age", "length_of_stay", "prior_admissions", "comorbidity_count", "medication_count", "followup_delay"], "means": [60, 5, 1, 2, 6, 10], "scales": [16, 2.5, 1.1, 1.4, 3, 6], "weights": [0.2, 0.25, 0.9, 0.7, 0.25, 0.45], "label": "simulated_readmission", "domain": "readmission", "description": "Build an admission-time-style tabular baseline for a simulated readmission outcome, with patient-level splitting and leakage audits.", "target": "simulated_readmission", "provenance": "synthetic mathematical simulator; not real clinical data"}')
FEATURES = SPEC["features"]
TARGET = SPEC["target"]
SEED = 42
