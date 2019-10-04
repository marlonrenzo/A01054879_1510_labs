from unittest import TestCase
from Lab04.time_calculator import time_calculator

class TestTimeCalculator(TestCase):
    def test_time_calculator_maximum(self):
        actual_value = time_calculator(31622399)
        expected_value = "365days, 23hours, 59minutes, 59seconds"
        self.assertEqual(actual_value, expected_value)

    def test_time_calculator_minimum(self):
        actual_value = time_calculator(0)
        expected_value = "0days, 0hours, 0minutes, 0seconds"
        self.assertEqual(actual_value, expected_value)

    def test_time_calculator_middle(self):
        actual_value = time_calculator(285803)
        expected_value = "3days, 7hours, 23minutes, 23seconds"
        self.assertEqual(actual_value, expected_value)

    def test_time_calculator_day(self):
        actual_value = time_calculator(86400)
        expected_value = "1days, 0hours, 0minutes, 0seconds"
        self.assertEqual(actual_value, expected_value)

    def test_time_calculator_hour(self):
        actual_value = time_calculator(3600)
        expected_value = "0days, 1hours, 0minutes, 0seconds"
        self.assertEqual(actual_value, expected_value)

    def test_time_calculator_minute(self):
        actual_value = time_calculator(60)
        expected_value = "0days, 0hours, 1minutes, 0seconds"
        self.assertEqual(actual_value, expected_value)

    def test_time_calculator_second(self):
        actual_value = time_calculator(59)
        expected_value = "0days, 0hours, 0minutes, 59seconds"
        self.assertEqual(actual_value, expected_value)









