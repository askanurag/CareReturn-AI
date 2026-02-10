# Synthetic demo data

`demo.csv`: 600 mathematical simulations with patient IDs and binary labels. `examples.csv`: five unlabeled rows for inference. `schema.json`: simulator specification. `data_dictionary.json`: per-field semantics. `split_manifest.json`: patient membership for seed 42.

Five cohort_seed CSVs are independent 120-row simulator draws. Five domain_sample CSVs illustrate raw signals or temporal records and are not linked to training-table patients. No real patient data. Target: simulated_readmission. These values are not validated physiologic reference ranges.

## Connected domain source files

Ten domain_record CSVs provide discharge snapshots and observed follow-up endpoints. All values, identifiers and outcomes are simulated. The domain cohort builder extracts features and labels using the documented units (days). These source records are unrelated to the original Gaussian demo patient IDs.
