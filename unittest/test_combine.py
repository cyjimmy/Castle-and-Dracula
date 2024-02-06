from unittest import TestCase
from game import combine


class TestCombine(TestCase):

    def test_valid_tuple(self):
        name = ("Name", "John")
        actual = combine(name)
        expected = "Name: John"
        self.assertEqual(actual, expected)
