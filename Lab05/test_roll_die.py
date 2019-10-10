from unittest import TestCase
from unittest.mock import patch
from Lab05.lab05 import roll_die


class TestRollDie(TestCase):
    @patch("random.randint", return_value=8)
    def test_roll_die(self, mock_output):
        actual_value = 8
        expected_value = mock_output.getvalue()
        self.assertEqual(actual_value, expected_value)
