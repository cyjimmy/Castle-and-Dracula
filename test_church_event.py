import io
from unittest import TestCase
from unittest.mock import patch
from game import church_event


class TestChurchEvent(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_character_with_hp_less_than_max(self, mock_output):
        character = {"Current HP": 7, "Max HP": 10}
        church_event(character)
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\nThe priest inside the church healed your wounds." \
                          "\nYour HP was fully restored.\n"
        self.assertEqual(expected_output, the_function_printed_this)
        expected_character = {"Current HP": 10, "Max HP": 10}
        self.assertEqual(expected_character, character)
