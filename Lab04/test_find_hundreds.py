from unittest import TestCase
from Lab04.roman_numbers import find_hundreds

class TestFind_hundreds(TestCase):
    def test_find_hundreds(self):
        actual_value = find_hundreds(299)
        expected_value = 2
        self.assertEqual(actual_value, expected_value)
