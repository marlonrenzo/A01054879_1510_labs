from unittest import TestCase
from Lab04.roman_numbers import replace_5_or_10

class TestReplace_5_or_10(TestCase):
    def test_replace_5_or_10_V(self):
        actual_value = replace_5_or_10(5, "I")
        expected_value = "V"
        self.assertEqual(actual_value, expected_value)

    def test_replace_5_or_10(self):
        actual_value = replace_5_or_10(10, "M")
        expected_value = "MMMMMMMMMM"
        self.assertEqual(actual_value, expected_value)


