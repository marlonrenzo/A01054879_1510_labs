from unittest import TestCase
from Lab04.time_calculator import format_time

class TestFormat_time(TestCase):
    def test_format_time(self):
        actual_value = format_time(5,6,8,10)
        expected_value = "5days, 6hours, 8minutes, 10seconds"
        self.assertEqual(actual_value, expected_value)