from unittest import TestCase
from Lab05.lab05 import generate_vowel


class TestGenerateVowel(TestCase):
    def test_generate_vowel(self):
        vowel = ['a', 'e', 'i', 'o', 'u', 'y']
        actual_value = generate_vowel()
        self.assertTrue(actual_value in vowel)
