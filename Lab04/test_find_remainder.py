from unittest import TestCase
from Lab04.time_calculator import find_remainder

class TestFind_remainder(TestCase):
    def test_find_remainder(self):
        actual_value = find_remainder(10,3,2)
        expected_value = 4
        self.assertEqual(actual_value, expected_value)
