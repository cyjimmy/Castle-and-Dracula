import io
from unittest import TestCase
from unittest.mock import patch
from game import hit_when_flee


class TestHitWhenFlee(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', return_value=10)
    def test_character_got_hit_when_flee(self, _, mock_output):
        foe = {"Attack": 3, "Name": "Assassin"}
        character = {"Current HP": 10}
        hit_when_flee(character, foe)
        expected_character = {"Current HP": 7}
        self.assertEqual(expected_character, character)
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\nYou got hit when you turned your back to Assassin.\n"
        self.assertEqual(expected_output, the_function_printed_this)

    @patch('random.randint', return_value=90)
    def test_character_did_not_get_hit_when_flee(self, _):
        foe = {"Attack": 5, "Name": "Assassin"}
        character = {"Current HP": 10}
        hit_when_flee(character, foe)
        expected_character = {"Current HP": 10}
        self.assertEqual(expected_character, character)
