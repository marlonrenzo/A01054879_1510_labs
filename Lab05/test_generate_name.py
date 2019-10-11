from unittest import TestCase
from Lab05.lab05 import generate_name
from unittest.mock import patch


class TestGenerateName(TestCase):
    def test_generate_name_length(self):
        actual_value = generate_name(18)
        name_length = len(actual_value)
        self.assertTrue(name_length == 36)

    def test_generate_name_vowel(self):
        vowel = ['a', 'e', 'i', 'o', 'u', 'y']
        actual_value = generate_name(10)
        self.assertTrue(actual_value[0] in vowel)

    def test_generate_name_consonant(self):
        consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
        actual_value = generate_name(10)
        self.assertTrue(actual_value[4] in consonant)
