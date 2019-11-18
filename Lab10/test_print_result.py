from unittest import TestCase
from Lab10.question_7 import print_result
from Lab10.question_7 import get_food_items
from unittest.mock import patch
import io


class TestPrintResult(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_result(self, mock_output):
        food = get_food_items()
        total_test = 12345
        avg_test = 54321.1
        keys = list(food.keys())
        expected = f"\nFood Items: {sorted(keys)}\nTotal Calories: {total_test} Average Calories: {avg_test}\n\n"
        print_result(keys, total_test, avg_test)
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)


