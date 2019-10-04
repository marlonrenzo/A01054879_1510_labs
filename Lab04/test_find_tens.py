from unittest import TestCase
from Lab04.roman_numbers import find_tens

class TestFind_tens(TestCase):
    def test_find_tens_maximum(self):
        actual_value = find_tens(99)
        expected_value = 9
        self.assertEqual(actual_value, expected_value)

    def test_find_tens_under(self):
        actual_value = find_tens(9)
        expected_value = 0
        self.assertEqual(actual_value, expected_value)

    def test_find_tens_middle(self):
        actual_value = find_tens(56)
        expected_value = 5
        self.assertEqual(actual_value, expected_value)
