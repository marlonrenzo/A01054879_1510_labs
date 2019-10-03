from unittest import TestCase
from Lab04.roman_numbers import find_ones

class TestFind_ones(TestCase):
    def test_find_ones(self):
        actual_value = find_ones(888)
        expected_value = 888
        self.assertEqual(actual_value, expected_value)
