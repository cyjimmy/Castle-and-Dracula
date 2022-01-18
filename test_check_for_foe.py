from unittest import TestCase
from unittest.mock import patch
from game import check_for_foe


class TestCheckForFoe(TestCase):

    @patch('random.randint', return_value=20)
    def test_random_number_less_than_26(self, _):
        actual = check_for_foe()
        expected = True
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=50)
    def test_random_number_more_than_26(self, _):
        actual = check_for_foe()
        expected = False
        self.assertEqual(expected, actual)
