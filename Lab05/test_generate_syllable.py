from unittest import TestCase
from Lab05.lab05 import generate_syllable
from unittest.mock import patch


class TestGenerateSyllable(TestCase):
    @patch("random.choice", return_value="op")
    def test_generate_syllable(self, mock_output):
        expected_value = "op"
        actual_value = generate_syllable()
        self.assertEqual(actual_value, expected_value)
