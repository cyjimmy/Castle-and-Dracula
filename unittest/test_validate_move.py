from unittest import TestCase
from game import validate_move


class TestValidateMove(TestCase):

    def test_move_within_board(self):
        board = {(0, 0): ".", (0, 1): ".", (0, 2): ".", (1, 0): ".", (1, 1): ".", (1, 2): "."}
        character = {"Coordinate": [0, 0]}
        direction = (1, 0)
        actual = validate_move(board, character, direction)
        expected = True
        self.assertEqual(expected, actual)

    def test_move_out_of_board(self):
        board = {(0, 0): ".", (0, 1): ".", (0, 2): ".", (1, 0): ".", (1, 1): ".", (1, 2): "."}
        character = {"Coordinate": [0, 2]}
        direction = (0, 1)
        actual = validate_move(board, character, direction)
        expected = False
        self.assertEqual(expected, actual)

    def test_new_coordinate_at_X(self):
        board = {(0, 0): ".", (0, 1): "X", (1, 0): ".", (1, 1): "."}
        character = {"Coordinate": [0, 0]}
        direction = (0, 1)
        actual = validate_move(board, character, direction)
        expected = False
        self.assertEqual(expected, actual)

    def test_arguments_unchanged(self):
        board = {(0, 0): ".", (0, 1): "X", (1, 0): ".", (1, 1): "."}
        character = {"Coordinate": [0, 0]}
        original_board = {(0, 0): ".", (0, 1): "X", (1, 0): ".", (1, 1): "."}
        original_character = {"Coordinate": [0, 0]}
        direction = (0, 1)
        validate_move(board, character, direction)
        self.assertEqual(original_board, board)
        self.assertEqual(original_character, character)
