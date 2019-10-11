from unittest import TestCase
from Lab05.lab05 import print_character
from unittest.mock import patch
import io

class TestPrintCharacter(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_character_no_inventory(self, mock_output):
        char = ['Jacilogo', ['Strength', 7], ['Dexterity', 4], ['Constitution', 8], ['Intelligence', 14], ['Wisdom', 4], ['Charisma', 13]]
        print_character(char)
        actual_value = mock_output.getvalue()
        expected_value = "Name: Jacilogo\nStrength: 7\nDexterity: 4\nConstitution: 8\nIntelligence: 14\nWisdom: 4\nCharisma: 13\n"
        self.assertEqual(actual_value, expected_value)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_character_with_inventory(self, mock_output):
        char = ['Jacilogo', ['Strength', 7], ['Dexterity', 4], ['Constitution', 8], ['Intelligence', 14], ['Wisdom', 4],
                ['Charisma', 13]]
        dummy_inventory = ["sword"]
        char.append(dummy_inventory)
        print_character(char)
        actual_value = mock_output.getvalue()
        expected_value = "Name: Jacilogo\nStrength: 7\nDexterity: 4\nConstitution: 8\nIntelligence: 14\nWisdom: 4\nCharisma: 13\n--Here are your inventory items--\nsword\n"
        self.assertEqual(actual_value, expected_value)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_character_incorrect_format(self, mock_output):
        char = ['Jacilogo', ['Strength', 7], ['Dexterity', 4], ['Constitution', 8], ['Charisma', 13]]
        print_character(char)
        actual_value = mock_output.getvalue()
        expected_value = "Warning: Error found with your list of character attributes\n"
        self.assertEqual(actual_value, expected_value)
