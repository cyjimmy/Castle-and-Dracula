import io
from unittest import TestCase
from unittest.mock import patch
from game import level_up


class TestLevelUp(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_character_level_up(self, mock_output):
        character = {"Exp": 3, "Level": 1, "Max HP": 5, "Current HP": 3, "Attack": 1, "Class": "Mage",
                     "Jobs": ["Mage", "Enchanter", "Wizard"], "Skills": ["Fire ball", "Thunderstorm", "Ice Wall"],
                     "Exp Needed": [3, 15]}
        level_up(character)
        expected_character = {"Exp": 3, "Level": 2, "Max HP": 15, "Current HP": 15, "Attack": 2, "Class": "Enchanter",
                              "Jobs": ["Mage", "Enchanter", "Wizard"],
                              "Skills": ["Fire ball", "Thunderstorm", "Ice Wall"], "Exp Needed": [3, 15]}
        self.assertEqual(expected_character, character)
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\nCongratulations! You level up to level 2.\n" \
                          "You have been promoted to Enchanter.\nMax HP, Attack increases.\n" \
                          "Current HP has been fully restored.\nYou have learnt Thunderstorm.\n"
        self.assertEqual(expected_output, the_function_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_character_level_up_twice(self, mock_output):
        character = {"Exp": 15, "Level": 1, "Max HP": 5, "Current HP": 3, "Attack": 1, "Class": "Mage",
                     "Jobs": ["Mage", "Enchanter", "Wizard"], "Skills": ["Fire ball", "Thunderstorm", "Ice Wall"],
                     "Exp Needed": [3, 15]}
        original_character = {"Exp": 15, "Level": 3, "Max HP": 25, "Current HP": 25, "Attack": 3, "Class": "Wizard",
                              "Jobs": ["Mage", "Enchanter", "Wizard"],
                              "Skills": ["Fire ball", "Thunderstorm", "Ice Wall"], "Exp Needed": [3, 15]}
        level_up(character)
        self.assertEqual(original_character, character)
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\nCongratulations! You level up to level 2.\n" \
                          "You have been promoted to Enchanter.\nMax HP, Attack increases.\n" \
                          "Current HP has been fully restored.\nYou have learnt Thunderstorm.\n" \
                          "\nCongratulations! You level up to level 3.\n" \
                          "You have been promoted to Wizard.\nMax HP, Attack increases.\n" \
                          "Current HP has been fully restored.\nYou have learnt Ice Wall.\n"
        self.assertEqual(expected_output, the_function_printed_this)

    def test_character_with_not_enough_exp(self):
        character = {"Exp": 12, "Level": 2, "Max HP": 5, "Current HP": 3, "Attack": 1, "Class": "Mage",
                     "Jobs": ["Mage", "Enchanter", "Wizard"], "Skills": ["Fire ball", "Thunderstorm", "Ice Wall"],
                     "Exp Needed": [3, 15]}
        original_character = {"Exp": 12, "Level": 2, "Max HP": 5, "Current HP": 3, "Attack": 1, "Class": "Mage",
                              "Jobs": ["Mage", "Enchanter", "Wizard"],
                              "Skills": ["Fire ball", "Thunderstorm", "Ice Wall"], "Exp Needed": [3, 15]}
        level_up(character)
        self.assertEqual(original_character, character)

    def test_max_level_character(self):
        character = {"Exp": 40, "Level": 3, "Max HP": 25, "Current HP": 25, "Attack": 3, "Class": "Wizard",
                     "Jobs": ["Mage", "Enchanter", "Wizard"],
                     "Skills": ["Fire ball", "Thunderstorm", "Ice Wall"], "Exp Needed": [3, 15]}
        original_character = {"Exp": 40, "Level": 3, "Max HP": 25, "Current HP": 25, "Attack": 3, "Class": "Wizard",
                              "Jobs": ["Mage", "Enchanter", "Wizard"],
                              "Skills": ["Fire ball", "Thunderstorm", "Ice Wall"], "Exp Needed": [3, 15]}
        level_up(character)
        self.assertEqual(original_character, character)
