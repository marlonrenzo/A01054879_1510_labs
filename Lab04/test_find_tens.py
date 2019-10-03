from unittest import TestCase
from Lab04.roman_numbers import find_tens

class TestFind_tens(TestCase):
    def test_find_tens(self):
        actual_value = find_tens(87)
        expected_value = 8
        self.assertEqual(actual_value, expected_value)
