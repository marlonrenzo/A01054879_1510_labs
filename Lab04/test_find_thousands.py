from unittest import TestCase
from Lab04.roman_numbers import find_thousands

class TestFind_thousands(TestCase):
    def test_find_thousands_maximum(self):
        actual_value = find_thousands(9999)
        expected_value = 9
        self.assertEqual(actual_value, expected_value)

    def test_find_thousands_under(self):
        actual_value = find_thousands(999)
        expected_value = 0
        self.assertEqual(actual_value, expected_value)

    def test_find_thousands_middle(self):
        actual_value = find_thousands(3560)
        expected_value = 3
        self.assertEqual(actual_value, expected_value)

