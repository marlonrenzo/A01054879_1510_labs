from unittest import TestCase
from Lab04.roman_numbers import final_conversion

class TestFinal_conversion(TestCase):
    def test_final_conversion(self):
        actual_value = final_conversion("M","","CM","","XC","","IX")
        expected_value = "MCMXCIX"
        self.assertEqual(actual_value, expected_value)

