from unittest import TestCase
from Lab07.midterm import list_tagger

class TestListTagger(TestCase):
    def test_list_tagger_empty_list(self):
        actual_value = list_tagger([])
        expected_value = [0]
        self.assertEqual(actual_value, expected_value)

    def test_list_tagger_one_element(self):
        actual_value = list_tagger([1])
        expected_value = [1, 1]
        self.assertEqual(actual_value, expected_value)

    def test_list_tagger_regular_list(self):
        actual_value = list_tagger([1, 2, 3, 4, 5, 6])
        expected_value = [6, 1, 2, 3, 4, 5, 6]
        self.assertEqual(actual_value, expected_value)

