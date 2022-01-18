import io
from unittest import TestCase
from unittest.mock import patch
from game import attack_blocked_message


class TestAttackBlockedMessage(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_wizard_class(self, mock_output):
        job = "Wizard"
        foe = {'Name': 'Dracula', 'Skill': 'Slap'}
        attack_blocked_message(job, foe)
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\nYour Ice shield blocks Dracula's Slap.\n"
        self.assertEqual(expected_output, the_function_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_berserker_class(self, mock_output):
        job = "Berserker"
        foe = {'Name': 'Assassin', 'Skill': 'Poke'}
        attack_blocked_message(job, foe)
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\nAssassin uses Poke on you, but you are not feeling anything.\n"
        self.assertEqual(expected_output, the_function_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_shadow_class(self, mock_output):
        job = "Shadow"
        foe = {'Name': 'Assassin', 'Skill': 'Poke'}
        attack_blocked_message(job, foe)
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\nAssassin uses Poke, but you are quick as the shadow and dodge the attack.\n"
        self.assertEqual(expected_output, the_function_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_other_class(self, mock_output):
        job = "Mastermind"
        foe = {'Name': 'Assassin', 'Skill': 'Poke'}
        attack_blocked_message(job, foe)
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\nAssassin is hypnotized, he does not know what he is doing.\n"
        self.assertEqual(expected_output, the_function_printed_this)

    def test_foe_unchanged(self):
        job = "Mastermind"
        foe = {'Name': 'Assassin', 'Skill': 'Poke'}
        original_foe = {'Name': 'Assassin', 'Skill': 'Poke'}
        attack_blocked_message(job, foe)
        self.assertEqual(original_foe, foe)
