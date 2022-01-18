import io
from unittest import TestCase
from unittest.mock import patch
from game import treasure_event


class TestTreasureEvent(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', return_value=75)
    def test_random_number_less_than_equals_to_80(self, _, mock_output):
        board = {(0, 0): ".", (0, 1): ".", (1, 0): ".", (1, 1): "T"}
        character = {"Max HP": 10, "Attack": 1, "Coordinate": [1, 1]}
        treasure_event(board, character)
        expected_character = {"Max HP": 15, "Attack": 1, "Coordinate": [1, 1]}
        self.assertEqual(expected_character, character)
        expected_board = {(0, 0): ".", (0, 1): ".", (1, 0): ".", (1, 1): "."}
        self.assertEqual(expected_board, board)
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\nAt the center of the ruin, you found an old tree." \
                          "\nThere was a mysterious glowing fruit on the tree. Out of curiosity, you ate the fruit." \
                          "\nSuddenly, You felt a surge of energy within your body.\nYour Max HP increased by 5.\n"
        self.assertEqual(expected_output, the_function_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', return_value=95)
    def test_random_number_greater_than_80(self, _, mock_output):
        board = {(0, 0): ".", (0, 1): ".", (1, 0): "T", (1, 1): "T"}
        character = {"Max HP": 10, "Attack": 1, "Coordinate": [1, 1]}
        treasure_event(board, character)
        expected_character = {"Max HP": 10, "Attack": 2, "Coordinate": [1, 1]}
        self.assertEqual(expected_character, character)
        expected_board = {(0, 0): ".", (0, 1): ".", (1, 0): "T", (1, 1): "."}
        self.assertEqual(expected_board, board)
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\nYou noticed a glowing object in the corner of the ruin." \
                          "\nIt was an enchanted ring! You did not know what the ring does, but you put it on anyway." \
                          "\nYou could feel the power stored within the ring flowing to your body." \
                          "\nYour attack power increased.\n"
        self.assertEqual(expected_output, the_function_printed_this)
