from unittest import TestCase
from Lab08.maze import show_position


class TestShowPosition(TestCase):
    def test_show_position(self):
        actual_value = show_position()
