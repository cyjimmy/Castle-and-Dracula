import io
from unittest import TestCase
from unittest.mock import patch
from game import make_foe


class TestMakeFoe(TestCase):

    def test_location_D(self):
        character = {"Level": 2}
        location = "D"
        actual = make_foe(character, location)
        expected = {"Name": "Dracula", "Current HP": 40, "Attack": 6,
                    "Skill": "Blood Edge", "Level": 3, "Accuracy": 0.9}
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_location_M(self, mock_output):
        character = {"Level": 2}
        location = "M"
        actual = make_foe(character, location)
        expected = {"Name": "Cyclops", "Current HP": 20, "Attack": 4,
                    "Skill": "Ground Slam", "Level": 3, "Accuracy": 0.6}
        self.assertEqual(expected, actual)
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\nYou have awaken a level 3 Cyclops!\n"
        self.assertEqual(expected_output, the_function_printed_this)

    @patch('random.randint', side_effect=[1, 5])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_location_dot_random_number_less_than_6(self, mock_output, _):
        character = {"Level": 1}
        location = "."
        actual = make_foe(character, location)
        expected = {"Name": "Barbarian", "Current HP": 4, "Attack": 1,
                    "Skill": "Cleave", "Level": 1, "Accuracy": 0.8}
        self.assertEqual(expected, actual)
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\nYou encountered a level 1 Barbarian!\n"
        self.assertEqual(expected_output, the_function_printed_this)

    @patch('random.randint', side_effect=[2, 7])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_location_dot_random_number_larger_than_5(self, mock_output, _):
        character = {"Level": 2}
        location = "."
        actual = make_foe(character, location)
        expected = {"Name": "Assassin", "Current HP": 9, "Attack": 4,
                    "Skill": "Swift Edge", "Level": 2, "Accuracy": 0.7}
        self.assertEqual(expected, actual)
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\nSuddenly a level 2 Assassin came out of nowhere!\n"
        self.assertEqual(expected_output, the_function_printed_this)
