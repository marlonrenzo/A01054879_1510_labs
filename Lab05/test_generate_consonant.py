from unittest import TestCase
from Lab05.lab05 import generate_consonant
from unittest.mock import patch


class TestGenerateConsonant(TestCase):
    def test_generate_consonant(self, mock_output):
        consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
        actual_value = generate_consonant()
        self.assertTrue(actual_value in consonant)
