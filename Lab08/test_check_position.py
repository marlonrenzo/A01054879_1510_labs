from unittest import TestCase
from Lab08.maze import check_position


class TestCheckPosition(TestCase):
    def test_check_position_doesnt_match(self):
        actual_value = check_position({"x": 0, "y": 0}, 4, 4)
        self.assertFalse(actual_value)

    def test_check_position_match(self):
        actual_value = check_position({"x": 4, "y": 4}, 4, 4)
        self.assertTrue(actual_value)

