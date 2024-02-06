from unittest import TestCase
from game import update_class_stats


class TestUpdateClassStats(TestCase):

    def test_character_warrior_class(self):
        character = {"Class": "Warrior"}
        update_class_stats(character)
        expected = {"Class": "Warrior", "Jobs": ["Warrior", "Knight", "Berserker"],
                    "Skills": ["Rising Slash", "Whirlwind", "Berserk mode"], "Exp Needed": [2, 10],
                    "Max HP": 15, "Current HP": 15, "Attack": 1, "Accuracy": 0.9, "Invincible": 0}
        self.assertEqual(expected, character)

    def test_character_thief_class(self):
        character = {"Class": "Thief"}
        update_class_stats(character)
        expected = {"Class": "Thief", "Jobs": ["Thief", "Assassin", "Shadow"],
                    "Skills": ["Assault Dive", "Divine Strike", "Shadow mode"], "Exp Needed": [4, 15],
                    "Max HP": 10, "Current HP": 10, "Attack": 3, "Accuracy": 0.8, "Invincible": 0}
        self.assertEqual(expected, character)

    def test_character_mage_class(self):
        character = {"Class": "Mage"}
        update_class_stats(character)
        expected = {"Class": "Mage", "Jobs": ["Mage", "Enchanter", "Wizard"],
                    "Skills": ["Fire ball", "Thunder Storm", "Ice shield"], "Exp Needed": [2, 10],
                    "Max HP": 8, "Current HP": 8, "Attack": 4, "Accuracy": 0.7, "Invincible": 0}
        self.assertEqual(expected, character)

    def test_character_illusionist_class(self):
        character = {"Class": "Illusionist"}
        update_class_stats(character)
        expected = {"Class": "Illusionist", "Jobs": ["Illusionist", "Mystic", "Mastermind"],
                    "Skills": ["Mind attack", "Terror Claw", "Hypnotize"], "Exp Needed": [3, 12],
                    "Max HP": 12, "Current HP": 12, "Attack": 2, "Accuracy": 0.8, "Invincible": 0}
        self.assertEqual(expected, character)
