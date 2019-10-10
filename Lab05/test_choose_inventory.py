from unittest import TestCase
from Lab05.lab05 import choose_inventory
from unittest.mock import patch


class TestChooseInventory(TestCase):
    @patch("random.sample", return_value=[1, 2])
    def test_choose_inventory_first(self, mock_output):
        inventory_test = ['one', 'two', 'three', 'four']
        expected_value = [1, 2]
        actual_value = choose_inventory(inventory_test, 2)
        self.assertEqual(actual_value, expected_value)

    @patch("random.sample", return_value=[2, 3])
    def test_choose_inventory_second(self, mock_output):
        inventory_test = ['one', 'two', 'three', 'four']
        expected_value = [2, 3]
        actual_value = choose_inventory(inventory_test, 2)
        self.assertEqual(actual_value, expected_value)

    @patch("random.sample", return_value=[0, 4])
    def test_choose_inventory_third(self, mock_output):
        inventory_test = ['one', 'two', 'three', 'four']
        expected_value = [0, 4]
        actual_value = choose_inventory(inventory_test, 2)
        self.assertEqual(actual_value, expected_value)
