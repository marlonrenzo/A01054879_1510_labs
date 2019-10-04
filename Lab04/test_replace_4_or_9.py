from unittest import TestCase
from Lab04.roman_numbers import replace_4_or_9

class TestReplace_4_or_9(TestCase):
    def test_replace_4_or_9_400(self):
        actual_value = replace_4_or_9(4, "C")
        expected_value = "CD"
        self.assertEqual(actual_value, expected_value)

    def test_replace_4_or_9_nine(self):
        actual_value = replace_4_or_9(9, "X")
        expected_value = "XC"
        self.assertEqual(actual_value, expected_value)
