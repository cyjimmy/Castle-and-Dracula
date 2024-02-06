import io
from unittest import TestCase
from unittest.mock import patch
from game import print_hp_message


class TestPrintHPMessage(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_message(self, mock_output):
        foe_info = {"Level": 3, "Name": "Dracula", "Current HP": 40}
        character_info = {"Current HP": 30}
        print_hp_message(foe_info, character_info)
        the_function_printed_this = mock_output.getvalue()
        expected = "\nLevel 3 Dracula has 40 HP left." \
                   "\nYou have 30 HP left.\n"
        self.assertEqual(expected, the_function_printed_this)
