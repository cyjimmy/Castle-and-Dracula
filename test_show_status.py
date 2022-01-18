import io
from unittest import TestCase
from unittest.mock import patch
from game import show_status


class TestShowStatus(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_not_max_character(self, mock_output):
        character = {"Coordinate": [1, 1], "Exp": 2, "HP": 5, "Class": "Shadow", "Exp Needed": [5, 13],
                     "Skills": ["A", "B", "C"], "Level": 1}
        show_status(character)
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\nHP : 5" \
                          "\nClass : Shadow" \
                          "\nLevel : 1" \
                          "\nExp to Next Level : 3" \
                          "\nSkill :" \
                          "\nA: Basic class attack. Low attack but high accuracy.\n"
        self.assertEqual(expected_output, the_function_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_max_level_character(self, mock_output):
        character = {"Coordinate": [1, 1], "Exp": 30, "HP": 5, "Class": "Shadow", "Exp Needed": [3, 13],
                     "Skills": ["A", "B", "C"], "Level": 3}
        show_status(character)
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\nHP : 5" \
                          "\nClass : Shadow" \
                          "\nLevel : 3" \
                          "\nSkill :" \
                          "\nA: Basic class attack. Low attack but high accuracy." \
                          "\nB: Advanced class skill with high attack but low accuracy." \
                          "\nC: Ultimate class skill that protects you from any attack for 2 rounds. This can only be" \
                          " used 2 times per fight.\n"
        self.assertEqual(expected_output, the_function_printed_this)

    def test_character_unchanged(self):
        character = {"Coordinate": [1, 1], "Exp": 3, "HP": 5, "Class": "Shadow", "Exp Needed": [3, 13],
                     "Skills": ["A", "B", "C"], "Level": 2}
        original_character = {"Coordinate": [1, 1], "Exp": 3, "HP": 5, "Class": "Shadow", "Exp Needed": [3, 13],
                              "Skills": ["A", "B", "C"], "Level": 2}
        show_status(character)
        self.assertEqual(original_character, character)
