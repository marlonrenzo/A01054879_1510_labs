from unittest import TestCase
from Lab08.maze import get_move
from unittest.mock import patch


class TestGetMove(TestCase):
    @patch("builtins.input", side_effect=["4"])
    def test_get_move_type(self, mock_output):
        actual_value = get_move()
        expected_value = 4
        self.assertEqual(actual_value, expected_value)

    @patch("builtins.input", side_effect=[1])
    def test_get_move_number(self, mock_output):
        actual_value = get_move()
        expected_value = 1
        self.assertEqual(actual_value, expected_value)