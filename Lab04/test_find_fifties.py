from unittest import TestCase
from Lab04.roman_numbers import find_fifties

class TestFind_fifties(TestCase):
    def test_find_fives(self):
        actual_value = find_fifties(54)
        expected_value = 1
        self.assertEqual(actual_value, expected_value)

    def test_find_hundreds_over(self):
        actual_value = find_fifties(92)
        expected_value = 0
        self.assertEqual(actual_value, expected_value)

    def test_find_hundreds_middle(self):
        actual_value = find_fifties(87)
        expected_value = 1
        self.assertEqual(actual_value, expected_value)


