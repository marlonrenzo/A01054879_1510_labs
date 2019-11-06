from unittest import TestCase
from Lab08.maze import move_character


class TestMoveCharacter(TestCase):
    def test_move_character_up(self):
        actual_value = move_character({"x": 1, "y": 1}, 1)
        expected_value = {'x': 1, 'y': 0}
        self.assertEqual(actual_value, expected_value)

    def test_move_character_down(self):
        actual_value = move_character({"x": 1, "y": 1}, 2)
        expected_value = {'x': 1, 'y': 2}
        self.assertEqual(actual_value, expected_value)

    def test_move_character_left(self):
        actual_value = move_character({"x": 1, "y": 1}, 3)
        expected_value = {'x': 0, 'y': 1}
        self.assertEqual(actual_value, expected_value)

    def test_move_character_right(self):
        actual_value = move_character({"x": 1, "y": 1}, 4)
        expected_value = {'x': 2, 'y': 1}
        self.assertEqual(actual_value, expected_value)
