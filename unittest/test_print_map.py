import io
from unittest import TestCase
from unittest.mock import patch
from game import print_map


class TestPrintMap(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_board(self, mock_output):
        rows = 3
        columns = 3
        character = {"Coordinate": [2, 0]}
        board = {(0, 0): ".", (0, 1): ".", (0, 2): ".",
                 (1, 0): ".", (1, 1): ".", (1, 2): ".",
                 (2, 0): ".", (2, 1): ".", (2, 2): "."}
        print_map(rows, columns, board, character)
        the_function_printed_this = mock_output.getvalue()
        expected = "\n. . ." \
                   "\n. . ." \
                   "\n\033[93m$\033[0m . ." \
                   "\nC:Church T:Treasure M:Elite Monster D:Castle Entrance\n"
        self.assertEqual(expected, the_function_printed_this)

    def test_character_unchanged(self):
        rows = 4
        columns = 4
        character = {"Coordinate": [2, 0]}
        original_character = {"Coordinate": [2, 0]}
        board = {(0, 0): ".", (0, 1): ".", (0, 2): ".", (0, 3): ".",
                 (1, 0): ".", (1, 1): ".", (1, 2): ".", (1, 3): ".",
                 (2, 0): ".", (2, 1): ".", (2, 2): ".", (2, 3): ".",
                 (3, 0): ".", (3, 1): ".", (3, 2): ".", (3, 3): "."}
        print_map(rows, columns, board, character)
        self.assertEqual(original_character, character)

    def test_board_unchanged(self):
        rows = 2
        columns = 2
        character = {"Coordinate": [1, 0]}
        board = {(0, 0): ".", (0, 1): ".",
                 (1, 0): ".", (1, 1): "."}
        original_board = {(0, 0): ".", (0, 1): ".",
                          (1, 0): ".", (1, 1): "."}
        print_map(rows, columns, board, character)
        self.assertEqual(original_board, board)
