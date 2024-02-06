from unittest import TestCase
from game import create_action_list


class TestCreateActionList(TestCase):

    def test_skills_list_length_equals_to_level(self):
        foe = "Barbarian"
        character = {"Skills": ["Skill 1", "Skill 2", "Skill 3"], "Level": 3, "Ultimate": 2}
        actual = create_action_list(character, foe)
        expected = ['Skill 1', 'Skill 2', 'Skill 3 (2 time left)', 'Flee']
        self.assertEqual(expected, actual)

    def test_skills_list_length_larger_than_level(self):
        foe = "Barbarian"
        character = {"Skills": ["Skill 1", "Skill 2", "Skill 3"], "Level": 1, "Ultimate": 2}
        actual = create_action_list(character, foe)
        expected = ['Skill 1', 'Flee']
        self.assertEqual(expected, actual)

    def test_foe_equals_dracula(self):
        foe = "Dracula"
        character = {"Skills": ["Skill 1", "Skill 2", "Skill 3"], "Level": 2, "Ultimate": 2}
        actual = create_action_list(character, foe)
        expected = ['Skill 1', "Skill 2"]
        self.assertEqual(expected, actual)

    def test_character_unchanged(self):
        foe = "Barbarian"
        character = {"Skills": ["Skill 1", "Skill 2", "Skill 3"], "Level": 1, "Ultimate": 2}
        original_character = {"Skills": ["Skill 1", "Skill 2", "Skill 3"], "Level": 1, "Ultimate": 2}
        create_action_list(character, foe)
        self.assertEqual(original_character, character)
