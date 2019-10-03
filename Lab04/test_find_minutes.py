from unittest import TestCase
from Lab04.time_calculator import find_minutes

class TestFind_minutes(TestCase):
    def test_find_minutes(self):
        actual_value = find_minutes(480)
        expected_value = 8
        self.assertEqual(actual_value, expected_value)
