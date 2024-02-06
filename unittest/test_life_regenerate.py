import io
from unittest import TestCase
from unittest.mock import patch
from game import life_regenerate


class TestLifeRegenerate(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_character_with_hp_less_than_max(self, mock_output):
        character = {"Current HP": 5, "Max HP": 10}
        life_regenerate(character)
        expected_character = {"Current HP": 6, "Max HP": 10}
        self.assertEqual(expected_character, character)
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\nRegenerate 1 HP.\n"
        self.assertEqual(expected_output, the_function_printed_this)

    def test_character_with_max_hp(self):
        character = {"Current HP": 10, "Max HP": 10}
        life_regenerate(character)
        expected_character = {"Current HP": 10, "Max HP": 10}
        self.assertEqual(expected_character, character)
