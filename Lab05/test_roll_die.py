from unittest import TestCase
from unittest.mock import patch
from Lab05.lab05 import roll_die


class TestRollDie(TestCase):
    @patch("random.randint", return_value=2)
    def test_roll_die_middle(self, mock_output):
        expected_value = 8
        actual_value = roll_die(4, 6)
        self.assertEqual(actual_value, expected_value)

    @patch("random.randint", return_value=12)
    def test_roll_die_high(self, mock_output):
        expected_value = 2304
        actual_value = roll_die(192, 17)
        self.assertEqual(actual_value, expected_value)

    @patch("random.randint", return_value=1)
    def test_roll_die_low(self, mock_output):
        expected_value = 1
        actual_value = roll_die(1, 1)
        self.assertEqual(actual_value, expected_value)