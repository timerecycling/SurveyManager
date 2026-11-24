import unittest
import math
import sys
import os

# Add the alpha_build directory to the path so we can import the modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../alpha_build')))

from calc_dist import haversine_distance
from calc_area import spherical_area

class TestMathFunctions(unittest.TestCase):
    def setUp(self):
        # London
        self.london = {"latitude": 51.5074, "longitude": -0.1278}
        # Paris
        self.paris = {"latitude": 48.8566, "longitude": 2.3522}
        # New York
        self.new_york = {"latitude": 40.7128, "longitude": -74.0060}

    def test_haversine_distance(self):
        # Test distance between London and Paris (~344km)
        dist = haversine_distance(self.london, self.paris)
        self.assertAlmostEqual(dist, 344000, delta=5000) 
        
        # Test distance to self
        self.assertEqual(haversine_distance(self.london, self.london), 0)

    def test_spherical_area(self):
        # Simple triangle
        coords = [self.london, self.paris, self.new_york]
        area = spherical_area(coords)
        self.assertGreater(area, 0)
        self.assertIsNone(spherical_area([self.london, self.paris]))

if __name__ == "__main__":
    unittest.main()
