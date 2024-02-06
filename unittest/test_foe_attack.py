import io
from unittest import TestCase
from unittest.mock import patch
from game import foe_attack


class TestFoeAttack(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', return_value=50)
    def test_foe_attack_hit_character(self, _, mock_output):
        foe = {"Accuracy": 0.7, "Attack": 3, "Name": "Assassin", "Skill": "Poke"}
        character = {"Current HP": 10, "Invincible": 0, "Class": "Shadow"}
        foe_attack(foe, character)
        expected_character = {"Current HP": 7, "Invincible": 0, "Class": "Shadow"}
        self.assertEqual(expected_character, character)
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\nAssassin uses Poke and deal 3 damage to you.\n"
        self.assertEqual(expected_output, the_function_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', return_value=100)
    def test_foe_attack_miss(self, _, mock_output):
        foe = {"Accuracy": 0.1, "Attack": 3, "Name": "Assassin", "Skill": "Poke"}
        character = {"Current HP": 10, "Invincible": 0, "Class": "Shadow"}
        foe_attack(foe, character)
        expected_character = {"Current HP": 10, "Invincible": 0, "Class": "Shadow"}
        self.assertEqual(expected_character, character)
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\nAssassin uses Poke, but he missed.\n"
        self.assertEqual(expected_output, the_function_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invincible_character(self, mock_output):
        foe = {"Accuracy": 0.7, "Attack": 7, "Name": "Assassin", "Skill": "Poke"}
        character = {"Current HP": 10, "Invincible": 1, "Class": "Berserker"}
        foe_attack(foe, character)
        expected_character = {"Current HP": 10, "Invincible": 0, "Class": "Berserker"}
        self.assertEqual(expected_character, character)
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\nAssassin uses Poke on you, but you are not feeling anything.\n"
        self.assertEqual(expected_output, the_function_printed_this)

    def test_foe_unchanged(self):
        foe = {"Accuracy": 0.7, "Attack": 7, "Name": "Assassin", "Skill": "Poke"}
        original_foe = {"Accuracy": 0.7, "Attack": 7, "Name": "Assassin", "Skill": "Poke"}
        character = {"Current HP": 10, "Invincible": 1, "Class": "Berserker"}
        foe_attack(foe, character)
        self.assertEqual(original_foe, foe)
