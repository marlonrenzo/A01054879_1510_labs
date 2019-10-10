from unittest import TestCase
from Lab05.lab05 import generate_consonant
from unittest.mock import patch


class TestGenerateConsonant(TestCase):
    @patch("random.choice", return_value="t")
    def test_generate_consonant(self, mock_output):
        expected_value = "t"
        actual_value = generate_consonant()
        self.assertEqual(actual_value, expected_value)
