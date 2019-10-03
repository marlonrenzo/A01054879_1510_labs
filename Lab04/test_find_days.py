from unittest import TestCase
from Lab04.time_calculator import find_days

class TestFind_days(TestCase):
    def test_find_days(self):
        actual_value = find_days(186400)
        expected_value = 2
        self.assertEqual(actual_value, expected_value)


