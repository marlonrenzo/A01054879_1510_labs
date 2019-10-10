from unittest import TestCase
from unittest.mock import patch
from Lab05.lab05 import roll_die


class TestRollDie(TestCase):
    @patch("random.randint", return_value=2)
    def test_roll_die(self, mock_output):
        expected_value = 8
        actual_value = roll_die(4, 6)
        self.assertEqual(actual_value, expected_value)
