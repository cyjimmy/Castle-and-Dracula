from unittest import TestCase
from game import move_character


class TestMoveCharacter(TestCase):

    def test_move_character(self):
        direction = (0, 1)
        character = {"Coordinate": [1, 1]}
        expected = {"Coordinate": [1, 2]}
        move_character(character, direction)
        self.assertEqual(expected, character)
