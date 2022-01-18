import io
from unittest import TestCase
from unittest.mock import patch
from game import make_character


class TestMakeCharacter(TestCase):

    @patch('builtins.input', side_effect=["Jimmy", "2"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_valid_input(self, mock_output, _):
        rows = 1
        actual = make_character(rows)
        expected = {"Name": "Jimmy", "Level": 1, "Class": "Thief", "Exp": 0, "Coordinate": [0, 0], "Ultimate": 2}
        self.assertEqual(expected, actual)
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\nBefore you start, please choose your class.\n" \
                          "1 Warrior: Well-trained fighter with sword and shield. Warrior has the highest HP and " \
                          "accuracy, but his attack is pretty bad.\n" \
                          "2 Thief: A deadly class that uses daggers to eliminate his targets. Thief has high " \
                          "accuracy and attack, but is low on HP.\n" \
                          "3 Mage: Specialized in destructive magic, mage is the strongest in attack. He can " \
                          "eliminate foes instantly if the attack actually lands. Mage has the lowest HP and accuracy" \
                          " in the game.\n" \
                          "4 Illusionist: All rounded caster, with average stats. There is really nothing special" \
                          " about this guy.\n"
        self.assertEqual(expected_output, the_function_printed_this)

    @patch('builtins.input', side_effect=["Jimmy", "66", "3"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_input(self, mock_output, _):
        rows = 5
        actual = make_character(rows)
        expected = {"Name": "Jimmy", "Level": 1, "Class": "Mage", "Exp": 0, "Coordinate": [4, 0], "Ultimate": 2}
        self.assertEqual(expected, actual)
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\nBefore you start, please choose your class.\n" \
                          "1 Warrior: Well-trained fighter with sword and shield. Warrior has the highest HP and " \
                          "accuracy, but his attack is pretty bad.\n" \
                          "2 Thief: A deadly class that uses daggers to eliminate his targets. Thief has high " \
                          "accuracy and attack, but is low on HP.\n" \
                          "3 Mage: Specialized in destructive magic, mage is the strongest in attack. He can " \
                          "eliminate foes instantly if the attack actually lands. Mage has the lowest HP and accuracy" \
                          " in the game.\n" \
                          "4 Illusionist: All rounded caster, with average stats. There is really nothing special" \
                          " about this guy.\n" \
                          "That is not a valid option. Please only enter the number shown in the list.\n" \
                          "\nBefore you start, please choose your class.\n" \
                          "1 Warrior: Well-trained fighter with sword and shield. Warrior has the highest HP and " \
                          "accuracy, but his attack is pretty bad.\n" \
                          "2 Thief: A deadly class that uses daggers to eliminate his targets. Thief has high " \
                          "accuracy and attack, but is low on HP.\n" \
                          "3 Mage: Specialized in destructive magic, mage is the strongest in attack. He can " \
                          "eliminate foes instantly if the attack actually lands. Mage has the lowest HP and accuracy" \
                          " in the game.\n" \
                          "4 Illusionist: All rounded caster, with average stats. There is really nothing special" \
                          " about this guy.\n"
        self.assertEqual(expected_output, the_function_printed_this)
