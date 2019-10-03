from unittest import TestCase
from Lab04.roman_numbers import find_five_hundreds

class TestFind_five_hundreds(TestCase):
    def test_find_five_hundreds(self):
        actual_value = find_five_hundreds(999)
        expected_value = 0
        self.assertEqual(actual_value, expected_value)
