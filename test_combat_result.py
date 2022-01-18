import io
from unittest import TestCase
from unittest.mock import patch
from game import combat_result


class TestCombatResult(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_character_won(self, mock_output):
        result = "win"
        foe = {"Name": "Cyclops", "Level": 5}
        character = {"Invincible": 2, "Ultimate": 1, "Exp": 0}
        combat_result(foe, character, result)
        expected_character = {"Invincible": 0, "Ultimate": 2, "Exp": 5}
        self.assertEqual(expected_character, character)
        this_function_printed_this = mock_output.getvalue()
        expected_output = "\nYou defeated Cyclops!\nYou gained 5 experience.\n"
        self.assertEqual(expected_output, this_function_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_character_fled(self, mock_output):
        result = "character flee"
        foe = {"Name": "Assassin", "Level": 5}
        character = {"Invincible": 1, "Ultimate": 1, "Exp": 0}
        combat_result(foe, character, result)
        expected_character = {"Invincible": 0, "Ultimate": 2, "Exp": 0}
        self.assertEqual(expected_character, character)
        this_function_printed_this = mock_output.getvalue()
        expected_output = "\nYou fled the fight.\n"
        self.assertEqual(expected_output, this_function_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_foe_fled(self, mock_output):
        result = "foe flee"
        foe = {"Name": "Cyclops", "Level": 5}
        character = {"Invincible": 0, "Ultimate": 2, "Exp": 0}
        combat_result(foe, character, result)
        expected_character = {"Invincible": 0, "Ultimate": 2, "Exp": 0}
        self.assertEqual(expected_character, character)
        this_function_printed_this = mock_output.getvalue()
        expected_output = "\nCyclops fled the fight.\n"
        self.assertEqual(expected_output, this_function_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_character_lose(self, mock_output):
        result = "lose"
        foe = {"Name": "Barbarian", "Level": 5}
        character = {"Invincible": 1, "Ultimate": 0, "Exp": 0}
        combat_result(foe, character, result)
        expected_character = {"Invincible": 0, "Ultimate": 2, "Exp": 0}
        self.assertEqual(expected_character, character)
        this_function_printed_this = mock_output.getvalue()
        expected_output = "\nYou died in the hand of Barbarian.\n"
        self.assertEqual(expected_output, this_function_printed_this)
