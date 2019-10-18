from unittest import TestCase
from Lab06.sparsevector import sparse_add


class TestSparseAdd(TestCase):
    def test_sparse_add_zeroes(self):
        actual_value = sparse_add({}, {})
        expected_value = {}
        self.assertEqual(actual_value, expected_value)

    def test_sparse_add_same_indices(self):
        actual_value = sparse_add({0: 5, 1: 5, 2: 5}, {0: 1, 1: 2, 2: 3})
        expected_value = {0: 6, 1: 7, 2: 8}
        self.assertEqual(actual_value, expected_value)

    def test_sparse_add_one_is_empty(self):
        actual_value = sparse_add({}, {1: 1, 10: 10, 30: 30})
        expected_value = {1: 1, 10: 10, 30: 30}
        self.assertEqual(actual_value, expected_value)

    def test_sparse_add_one_is_empty_two(self):
        actual_value = sparse_add({2: 4, 6: 8, 3: 5}, {})
        expected_value = {2: 4, 6: 8, 3: 5}
        self.assertEqual(actual_value, expected_value)

    def test_sparse_add_no_info_matching(self):
        actual_value = sparse_add({0: 1, 3: 4, 6: 5}, {2: 1, 4: 7, 10: 4})
        expected_value = {0: 1, 3: 4, 6: 5, 2: 1, 4: 7, 10: 4}
        self.assertEqual(actual_value, expected_value)

    def test_sparse_add_some_matching(self):
        actual_value = sparse_add({0: 4, 1: 5, 2: 7}, {0: 3, 1: 4, 3: 9})
        expected_value = {0: 7, 1: 9, 2: 7, 3: 9}
        self.assertEqual(actual_value, expected_value)

    def test_sparse_add_to_zero(self):
        actual_value = sparse_add({0: -5, 4: -3}, {0: 5, 4: 3})
        expected_value = {}
        self.assertEqual(actual_value, expected_value)
