from unittest import TestCase
from Lab04.roman_numbers import find_thousands

class TestFind_thousands(TestCase):
    def test_find_thousands(self):
        actual_value = find_thousands(8796)
        expected_value = 8
        self.assertEqual(actual_value, expected_value)
        
