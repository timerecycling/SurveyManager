import unittest
import math
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../alpha_build')))

from csv_exporter import export_to_csv
from validator import validate_survey_data
from calc_dist import haversine_distance
from calc_area import spherical_area

class TestSurveyManager(unittest.TestCase):
    def setUp(self):
        self.coords_dict = {
            "A": {"coordname": "A", "latitude": 51.5074, "longitude": -0.1278, "order": 1},
            "B": {"coordname": "B", "latitude": 48.8566, "longitude": 2.3522, "order": 2}
        }

    def test_validator_detailed(self):
        # Test 1: Valid
        is_valid, msg = validate_survey_data(self.coords_dict)
        print(f"Test 1 (Valid): is_valid={is_valid}, msg={msg}")
        self.assertTrue(is_valid)
        
        # Test 2: Missing key
        bad_coords = {"A": {"coordname": "A", "latitude": 10.0}}
        is_valid, msg = validate_survey_data(bad_coords)
        print(f"Test 2 (Invalid): is_valid={is_valid}, msg={msg}")
        self.assertFalse(is_valid)

if __name__ == "__main__":
    unittest.main()
