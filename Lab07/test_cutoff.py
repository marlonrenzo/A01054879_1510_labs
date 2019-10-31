from unittest import TestCase
from Lab07.midterm import cutoff


class TestCutoff(TestCase):
    def test_cutoff_empty_list_and_zero(self):
        actual_value = cutoff([], 0)
        expected_value = 0
        self.assertEqual(actual_value, expected_value)

    def test_cutoff_empty_list_and_five(self):
        actual_value = cutoff([], 5)
        expected_value = 0
        self.assertEqual(actual_value, expected_value)

    def test_cutoff_list_with_zero_and_zero(self):
        actual_value = cutoff([0], 0)
        expected_value = 0
        self.assertEqual(actual_value, expected_value)

    def test_cutoff_list_with_2_and_2(self):
        actual_value = cutoff([2], 2)
        expected_value = 1
        self.assertEqual(actual_value, expected_value)

    def test_cutoff_list_with_2_and_4(self):
        actual_value = cutoff([2], 4)
        expected_value = 0
        self.assertEqual(actual_value, expected_value)

    def test_cutoff_list_with_5_integers_and_0(self):
        actual_value = cutoff([1, 2, 3, 4, 5], 0)
        expected_value = 0
        self.assertEqual(actual_value, expected_value)

    def test_cutoff_list_with_5_integers_and_2(self):
        actual_value = cutoff([1, 2, 3, 4, 5], 2)
        expected_value = 2
        self.assertEqual(actual_value, expected_value)

    def test_cutoff_list_5_integers_and_same_integer(self):
        actual_value = cutoff([2, 2, 2, 2, 2], 2)
        expected_value = 5
        self.assertEqual(actual_value, expected_value)

    def test_cutoff_list_5_integers_and_larger_integer(self):
        actual_value = cutoff([2, 2, 2, 2, 2], 0)
        expected_value = 0
        self.assertEqual(actual_value, expected_value)

    def test_cutoff_5_multiples_and_increment(self):
        actual_value = cutoff([3, 6, 9, 12, 15], 3)
        expected_value = 5
        self.assertEqual(actual_value, expected_value)

    def test_cutoff_5_negative_multiples_and_increment(self):
        actual_value = cutoff([-3, -6, -9, -12], 3)
        expected_value = 4
        self.assertEqual(actual_value, expected_value)
