from unittest import TestCase
from game import get_vector


class TestGetVector(TestCase):

    def test_command_up(self):
        command = "Up"
        actual = get_vector(command)
        expected = (-1, 0)
        self.assertEqual(expected, actual)

    def test_command_down(self):
        command = "Down"
        actual = get_vector(command)
        expected = (1, 0)
        self.assertEqual(expected, actual)

    def test_command_left(self):
        command = "Left"
        actual = get_vector(command)
        expected = (0, -1)
        self.assertEqual(expected, actual)

    def test_command_right(self):
        command = "Right"
        actual = get_vector(command)
        expected = (0, 1)
        self.assertEqual(expected, actual)
