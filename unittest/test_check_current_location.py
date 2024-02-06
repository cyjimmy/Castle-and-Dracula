from unittest import TestCase
from game import check_current_location


class TestCheckCurrentLocation(TestCase):

    def test_check_location(self):
        board = {(0, 0): "D", (0, 1): ".", (1, 0): ".", (1, 1): "."}
        character = {"Coordinate": [0, 0]}
        actual = check_current_location(board, character)
        expected = 'D'
        self.assertEqual(expected, actual)

    def test_arguments_unchanged(self):
        board = {(0, 0): "D", (0, 1): ".", (1, 0): ".", (1, 1): "."}
        character = {"Coordinate": [0, 0]}
        original_board = {(0, 0): "D", (0, 1): ".", (1, 0): ".", (1, 1): "."}
        original_character = {"Coordinate": [0, 0]}
        check_current_location(board, character)
        self.assertEqual(original_board, board)
        self.assertEqual(original_character, character)
