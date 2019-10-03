from unittest import TestCase
from Lab04.roman_numbers import convert_to_roman_numeral

class TestConvert_to_roman_numeral(TestCase):
    def test_convert_to_roman_numeral(self):
        actual_value = convert_to_roman_numeral(4999)
        expected_value = "MMMMCMXCIX"
        self.assertEqual(actual_value, expected_value)

