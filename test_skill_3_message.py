import io
from unittest import TestCase
from unittest.mock import patch
from game import skill_3_message


class TestSkill3Message(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_berserker_class(self, mock_output):
        character = "Berserker"
        foe = "Barbarian"
        skill_3_message(character, foe)
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\nYou are in Berserk mode now. You will not take any damage for 2 rounds.\n"
        self.assertEqual(expected_output, the_function_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_shadow_class(self, mock_output):
        character = "Shadow"
        foe = "Barbarian"
        skill_3_message(character, foe)
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\nYou are in Shadow mode now. Your speed dramatically increases for 2 rounds.\n"
        self.assertEqual(expected_output, the_function_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_wizard_class(self, mock_output):
        character = "Wizard"
        foe = "Barbarian"
        skill_3_message(character, foe)
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\nYou have casted an Ice shield. This shield will protect you for 2 rounds.\n"
        self.assertEqual(expected_output, the_function_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_other_class(self, mock_output):
        character = "MasterMind"
        foe = "Barbarian"
        skill_3_message(character, foe)
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\nYou have Hypnotize the Barbarian. He will not attack you for 2 rounds.\n"
        self.assertEqual(expected_output, the_function_printed_this)
