import unittest,tempfile
from pathlib import Path
import numpy as np
from healthcare_ai.domain_simulation import make_recording

class TestCase(unittest.TestCase):
    def setUp(self):
        self.record=make_recording(7)

    def test_behavior(self):
        from healthcare_ai.domain_preprocess import prepare_encounters
        import pandas as pd
        f=prepare_encounters(self.record);self.assertTrue(pd.api.types.is_datetime64_any_dtype(f.discharge_time))
        f=self.record.copy();f.loc[0,'feature_time']='2035-01-01'
        with self.assertRaises(ValueError):prepare_encounters(f)

if __name__=="__main__":unittest.main()
