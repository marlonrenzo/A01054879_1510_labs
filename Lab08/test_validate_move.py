from unittest import TestCase
from Lab08.maze import validate_move


class TestValidateMove(TestCase):
    def test_validate_move_right_min_x(self):
        actual_value = validate_move({"x": 0, "y": 2}, 4)
        self.assertTrue(actual_value)

    def test_validate_move_right_max_x(self):
        actual_value = validate_move({"x": 4, "y": 3}, 4)
        self.assertFalse(actual_value)

    def test_validate_move_up_max_x(self):
        actual_value = validate_move({"x": 0, "y": 4}, 1)
        self.assertTrue(actual_value)

    def test_validate_move_right_up_min_x(self):
        actual_value = validate_move({"x": 4, "y": 3}, 4)
        self.assertFalse(actual_value)

