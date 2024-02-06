from unittest import TestCase
from unittest.mock import patch
from game import combat


class TestCombat(TestCase):

    @patch('builtins.input', side_effect=["1"])
    @patch('random.randint', side_effect=[1])
    def test_character_win(self, _, __):
        foe = {"Name": "Barbarian", "Current HP": 4, "Attack": 1, "Skill": "Cleave", "Level": 1, "Accuracy": 1}
        character = {"Class": "Warrior", "Jobs": ["Warrior", "Knight", "Berserker"], "Level": 3, "Ultimate": 2,
                     "Skills": ["Rising Slash", "Whirlwind", "Berserk mode"], "Max HP": 15, "Current HP": 15,
                     "Attack": 100, "Accuracy": 1, "Invincible": 0}
        actual = combat(foe, character)
        expected = "win"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["1"])
    @patch('random.randint', side_effect=[1, 1, 30])
    def test_character_die(self, _, __):
        foe = {"Name": "Barbarian", "Current HP": 4, "Attack": 100, "Skill": "Cleave", "Level": 1, "Accuracy": 1}
        character = {"Class": "Warrior", "Jobs": ["Warrior", "Knight", "Berserker"], "Level": 3, "Ultimate": 2,
                     "Skills": ["Rising Slash", "Whirlwind", "Berserk mode"], "Max HP": 15, "Current HP": 15,
                     "Attack": 1, "Accuracy": 1, "Invincible": 0}
        actual = combat(foe, character)
        expected = "die"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["4"])
    @patch('random.randint', side_effect=[1, 1, 100])
    def test_character_flee(self, _, __):
        foe = {"Name": "Barbarian", "Current HP": 4, "Attack": 1, "Skill": "Cleave", "Level": 1, "Accuracy": 1}
        character = {"Class": "Warrior", "Jobs": ["Warrior", "Knight", "Berserker"], "Level": 3, "Ultimate": 1,
                     "Skills": ["Rising Slash", "Whirlwind", "Berserk mode"], "Max HP": 15, "Current HP": 15,
                     "Attack": 1, "Accuracy": 1, "Invincible": 0}
        actual = combat(foe, character)
        expected = "character flee"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["1"])
    @patch('random.randint', side_effect=[1, 1, 20])
    def test_foe_flee(self, _, __):
        foe = {"Name": "Thief", "Current HP": 4, "Attack": 1, "Skill": "Cleave", "Level": 1, "Accuracy": 1}
        character = {"Class": "Warrior", "Jobs": ["Warrior", "Knight", "Berserker"], "Level": 2, "Ultimate": 2,
                     "Skills": ["Rising Slash", "Whirlwind", "Berserk mode"], "Max HP": 15, "Current HP": 15,
                     "Attack": 1, "Accuracy": 1, "Invincible": 0}
        actual = combat(foe, character)
        expected = "foe flee"
        self.assertEqual(expected, actual)
