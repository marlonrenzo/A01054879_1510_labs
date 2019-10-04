from unittest import TestCase
from Lab04.roman_numbers import convert_to_roman_numeral

class TestConvert_to_roman_numeral(TestCase):
    def test_convert_to_roman_numeral_max(self):
        actual_value = convert_to_roman_numeral(10000)
        expected_value = "MMMMMMMMMM"
        self.assertEqual(actual_value, expected_value)

    def test_convert_to_roman_numeral_over_max(self):
        actual_value = convert_to_roman_numeral(10001)
        expected_value = None
        self.assertEqual(actual_value, expected_value)

    def test_convert_to_roman_numeral_zero(self):
        actual_value = convert_to_roman_numeral(0)
        expected_value = ""
        self.assertEqual(actual_value, expected_value)

    def test_convert_to_roman_numeral_4(self):
        actual_value = convert_to_roman_numeral(4)
        expected_value = "IV"
        self.assertEqual(actual_value, expected_value)

    def test_convert_to_roman_numeral_49(self):
        actual_value = convert_to_roman_numeral(49)
        expected_value = "XLIX"
        self.assertEqual(actual_value, expected_value)

    def test_convert_to_roman_numeral_9(self):
        actual_value = convert_to_roman_numeral(9)
        expected_value = "IX"
        self.assertEqual(actual_value, expected_value)

    def test_convert_to_roman_numeral_499(self):
        actual_value = convert_to_roman_numeral(499)
        expected_value = "CDXIX"
        self.assertEqual(actual_value, expected_value)

    def test_convert_to_roman_numeral_50(self):
        actual_value = convert_to_roman_numeral(50)
        expected_value = "L"
        self.assertEqual(actual_value, expected_value)

    def test_convert_to_roman_numeral_67(self):
        actual_value = convert_to_roman_numeral(67)
        expected_value = "LXVII"
        self.assertEqual(actual_value, expected_value)

