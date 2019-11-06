from unittest import TestCase
from Lab08.maze import check_reached_goal
from unittest.mock import patch
import io


class TestCheckReachedGoal(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_check_reached_goal_false(self, mock_output):
        check_reached_goal({"x": 0, "y": 0}, 0)
        actual_value = mock_output.getvalue()
        expected_value = 'Keep going! I believe in you!\n'
        self.assertEqual(actual_value, expected_value)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_check_reached_goal_true(self, mock_output):
        check_reached_goal({"x": 4, "y": 4}, 1)
        actual_value = mock_output.getvalue()
        expected_value = '\n\n[ ] [ ] [ ] [ ] [ ] \n\n' \
                             '[ ] [ ] [ ] [ ] [ ] \n\n' \
                             '[ ] [ ] [ ] [ ] [ ] \n\n' \
                             '[ ] [ ] [ ] [ ] [ ] \n\n' \
                             '[ ] [ ] [ ] [ ] [x] \n\n' \
                             'Congratulations! You are a master of this maze!\n'
        self.assertEqual(actual_value, expected_value)



