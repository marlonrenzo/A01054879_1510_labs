from unittest import TestCase
from Lab07.midterm import prepender


class TestPrepender(TestCase):
    def test_prepender_empty_list_and_empty_string(self):
        actual_value = prepender([], "")
        expected_value = []
        self.assertEqual(actual_value, expected_value)

    def test_prepender_empty_list_and_non_empty_string(self):
        actual_value = prepender([], "Python")
        expected_value = []
        self.assertEqual(actual_value, expected_value)

    def test_prepender_non_empty_list_and_empty_string(self):
        actual_value = prepender(["Python"], "")
        expected_value = ["Python"]
        self.assertEqual(actual_value, expected_value)

    def test_prepender_non_empty_list_and_non_empty_string(self):
        actual_value = prepender(["Python"], "I love ")
        expected_value = ["I love Python"]
        self.assertEqual(actual_value, expected_value)

    def test_prepender_list_with_multiple_strings_and_empty_string(self):
        actual_value = prepender(["Python", "is", "better", "than", "JavaScript"], "")
        expected_value = ["Python", "is", "better", "than", "JavaScript"]
        self.assertEqual(actual_value, expected_value)

    def test_prepender_list_with_multiple_strings_and_non_empty_string(self):
        actual_value = prepender(["Python", "is", "better", "than", "JavaScript"], "Umm... ")
        expected_value = ["Umm... Python", "Umm... is", "Umm... better", "Umm... than", "Umm... JavaScript"]
        self.assertEqual(actual_value, expected_value)