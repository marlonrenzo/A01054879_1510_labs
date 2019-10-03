from unittest import TestCase
from Lab04.time_calculator import find_hours

class TestFind_hours(TestCase):
    def test_find_hours(self):
        actual_value = find_hours(360000)
        expected_value = 100
        self.assertEqual(actual_value, expected_value)


