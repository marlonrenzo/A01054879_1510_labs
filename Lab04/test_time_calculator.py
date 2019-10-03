from unittest import TestCase
from Lab04.time_calculator import time_calculator

class test_time_calculator(TestCase):
    def test_find_remainder(self):
        actual_value = time_calculator(59)
        expected_value = "0days, 0hours, 0minutes, 59seconds"
        self.assertEqual(actual_value, expected_value)

