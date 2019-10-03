from unittest import TestCase
from Lab04.roman_numbers import find_fives

class TestFind_fives(TestCase):
    def test_find_fives(self):
        actual_value = find_fives(8)
        expected_value = 1
        self.assertEqual(actual_value, expected_value)

