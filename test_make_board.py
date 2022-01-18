from unittest import TestCase
from unittest.mock import patch
from game import make_board


class TestMakeBoard(TestCase):

    @patch('random.randint', side_effect=[1, 2, 5, 10, 10, 100])
    def test_different_random_number(self, _):
        rows = 3
        columns = 2
        actual = make_board(rows, columns)
        expected = {(0, 0): "C", (0, 1): "T", (1, 0): "M", (1, 1): ".",
                    (2, 0): ".", (2, 1): "."}
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[1, 3, 5, 5, 1, 3, 5, 5, 1, 3, 5, 5])
    def test_event_sequence(self, _):
        rows = 3
        columns = 4
        actual = make_board(rows, columns)
        expected = {(0, 0): "C", (0, 1): "T", (0, 2): "M", (0, 3): "M",
                    (1, 0): "C", (1, 1): "T", (1, 2): "M", (1, 3): "M",
                    (2, 0): ".", (2, 1): "T", (2, 2): "M", (2, 3): "M"}
        self.assertEqual(expected, actual)
