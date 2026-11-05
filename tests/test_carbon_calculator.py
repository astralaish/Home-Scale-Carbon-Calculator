import unittest
import sys
import os

# This line ensures Python can find 'carbon_calculator.py' in the parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from carbon_calculator import calculate_annual_emissions

class CarbonCalculatorTests(unittest.TestCase):
    def setUp(self):
        self.factors = {
            "Transport": 0.14,
            "Electricity": 0.68,
            "Diet": 1.25,
            "Waste": 0.10,
        }

    def test_zero_inputs_return_zero(self):
        result = calculate_annual_emissions(0, 0, 0, 0, self.factors)
        self.assertEqual(result["total_tonnes"], 0)

    def test_annualisation_and_category_values(self):
        result = calculate_annual_emissions(1, 10, 2, 1, self.factors)
        self.assertAlmostEqual(result["category_kg"]["transport"], 51.1)
        self.assertAlmostEqual(result["category_kg"]["electricity"], 81.6)
        self.assertAlmostEqual(result["category_kg"]["waste"], 10.4)
        self.assertAlmostEqual(result["category_kg"]["diet"], 456.25)

    def test_negative_input_is_rejected(self):
        with self.assertRaises(ValueError):
            calculate_annual_emissions(-1, 0, 0, 0, self.factors)

    def test_missing_factor_is_rejected(self):
        with self.assertRaises(ValueError):
            calculate_annual_emissions(1, 1, 1, 1, {"Transport": 0.14})

if __name__ == "__main__":
    unittest.main()