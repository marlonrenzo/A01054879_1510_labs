from unittest import TestCase
from Lab05.lab05 import generate_vowel
from unittest.mock import patch


class TestGenerateVowel(TestCase):
    @patch("random.choice", return_value="e")
    def test_generate_vowel(self, mock_output):
        expected_value = "e"
        actual_value = generate_vowel()
        self.assertEqual(actual_value, expected_value)
