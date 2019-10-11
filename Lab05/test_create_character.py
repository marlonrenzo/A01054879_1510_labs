from unittest import TestCase
from Lab05.lab05 import create_character


class TestCreateCharacter(TestCase):
    def test_create_character_list_length(self):
        actual_value = create_character(10)
        self.assertTrue(len(actual_value) == 7)

    def test_create_character_attribute_strength(self):
        list = create_character(10)
        actual_value = list[1][0]
        expected_value = "Strength"
        self.assertEqual(actual_value, expected_value)

    def test_create_character_attribute_charisma(self):
        character = create_character(10)
        actual_value = character[6][0]
        expected_value = "Charisma"
        self.assertEqual(actual_value, expected_value)

    def test_create_character_name_length(self):
        actual_value = create_character(28)
        name_length = len(actual_value[0])
        self.assertTrue(name_length == 28)

