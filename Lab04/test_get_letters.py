from unittest import TestCase
from Lab04.roman_numbers import get_letters

class TestGet_letters(TestCase):
    def test_get_letters_(self):
        actual_value = get_letters(3, "I")
        expected_value = "III"
        self.assertEqual(actual_value, expected_value)

    def test_get_letters_800(self):
        actual_value = get_letters(8, "C")
        expected_value = "CCCCCCCC"
        self.assertEqual(actual_value, expected_value)

    def test_get_letters(self):
        actual_value = get_letters(9, "I")
        expected_value = "IX"
        self.assertEqual(actual_value, expected_value)

    def test_get_letters(self):
        actual_value = get_letters(4, "C")
        expected_value = "CD"
        self.assertEqual(actual_value, expected_value)


