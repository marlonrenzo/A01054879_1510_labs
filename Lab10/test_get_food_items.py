from unittest import TestCase
from Lab10.question_7 import get_food_items


class TestGetFoodItems(TestCase):
    def test_get_food_items_type(self):
        actual = type(get_food_items())
        expected = dict
        self.assertEqual(actual, expected)

    def test_get_food_items_values(self):
        actual = get_food_items()
        values = []
        expected = int
        for i in actual.values():
            values.append(i)
        for thing in values:
            self.assertEqual(type(thing), expected)

    def test_get_food_items_keys(self):
        actual = get_food_items()
        keys = []
        expected = str
        for i in actual.keys():
            keys.append(i)
        for thing in keys:
            self.assertEqual(type(thing), expected)
