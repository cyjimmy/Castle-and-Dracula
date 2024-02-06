import io
from unittest import TestCase
from unittest.mock import patch
from game import character_skill_effect


class TestCharacterSkillEffect(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', return_value=85)
    def test_character_skill_1_hit_foe(self, _, mock_output):
        skill = "Kick"
        foe = {"Name": "Dracula", "Current HP": 10}
        character = {"Skills": ["Kick", "Slash", "Block"], "Accuracy": 0.9, "Attack": 5, "Invincible": 0,
                     "Ultimate": 2, "Class": "Shadow"}
        character_skill_effect(skill, foe, character)
        expected_foe = {"Name": "Dracula", "Current HP": 5}
        self.assertEqual(expected_foe, foe)
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\nYour Kick deal 5 damage to Dracula.\n"
        self.assertEqual(expected_output, the_function_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', return_value=50)
    def test_character_skill_2_hit_foe(self, _, mock_output):
        skill = "Slash"
        foe = {"Name": "Dracula", "Current HP": 10}
        character = {"Skills": ["Kick", "Slash", "Block"], "Accuracy": 0.9, "Attack": 5, "Invincible": 0,
                     "Ultimate": 2, "Class": "Shadow"}
        character_skill_effect(skill, foe, character)
        expected_foe = {"Name": "Dracula", "Current HP": 0}
        self.assertEqual(expected_foe, foe)
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\nYour Slash deal 10 damage to Dracula.\n"
        self.assertEqual(expected_output, the_function_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', return_value=100)
    def test_character_miss(self, _, mock_output):
        skill = "Scratch"
        foe = {"Name": "Dracula", "Current HP": 10}
        character = {"Skills": ["Kick", "Slash", "Block"], "Accuracy": 0.9, "Attack": 5, "Invincible": 0,
                     "Ultimate": 2, "Class": "Shadow"}
        character_skill_effect(skill, foe, character)
        expected_foe = {"Name": "Dracula", "Current HP": 10}
        self.assertEqual(expected_foe, foe)
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\nYou tried to use Scratch on Dracula, but you missed.\n"
        self.assertEqual(expected_output, the_function_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_character_ultimate(self, mock_output):
        skill = "Block"
        foe = {"Name": "Dracula", "Current HP": 100}
        character = {"Skills": ["Kick", "Slash", "Block"], "Accuracy": 0.9, "Attack": 5, "Invincible": 0,
                     "Ultimate": 2, "Class": "Shadow"}
        character_skill_effect(skill, foe, character)
        expected_foe = {"Name": "Dracula", "Current HP": 100}
        self.assertEqual(expected_foe, foe)
        expected_character = {"Skills": ["Kick", "Slash", "Block"], "Accuracy": 0.9, "Attack": 5, "Invincible": 2,
                              "Ultimate": 1, "Class": "Shadow"}
        self.assertEqual(expected_character, character)
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\nYou are in Shadow mode now. Your speed dramatically increases for 2 rounds.\n"
        self.assertEqual(expected_output, the_function_printed_this)
