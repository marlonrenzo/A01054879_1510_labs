from unittest import TestCase
from Lab04.roman_numbers import find_fifties

class TestFind_fifties(TestCase):
    def test_find_fifties(self):
        actual_value = find_fifties(89)
        expected_value = 1
        self.assertEqual(actual_value, expected_value)


