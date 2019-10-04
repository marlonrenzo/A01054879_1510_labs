from unittest import TestCase
from Lab04.roman_numbers import find_hundreds

class TestFind_hundreds(TestCase):
    def test_find_hundreds_maximum(self):
        actual_value = find_hundreds(999)
        expected_value = 9
        self.assertEqual(actual_value, expected_value)

    def test_find_hundreds_under(self):
        actual_value = find_hundreds(99)
        expected_value = 0
        self.assertEqual(actual_value, expected_value)

    def test_find_hundreds_middle(self):
        actual_value = find_hundreds(356)
        expected_value = 3
        self.assertEqual(actual_value, expected_value)