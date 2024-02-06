from unittest import TestCase
from game import check_goal_attained


class TestCheckGoalAttained(TestCase):

    def test_win_not_at_location_D(self):
        location = "."
        result = "win"
        actual = check_goal_attained(location, result)
        expected = False
        self.assertEqual(expected, actual)

    def test_lose_not_at_location_D(self):
        location = "."
        result = "lose"
        actual = check_goal_attained(location, result)
        expected = False
        self.assertEqual(expected, actual)

    def test_win_at_location_D(self):
        location = "D"
        result = "win"
        actual = check_goal_attained(location, result)
        expected = True
        self.assertEqual(expected, actual)

    def test_lose_at_location_D(self):
        location = "D"
        result = "lose"
        actual = check_goal_attained(location, result)
        expected = False
        self.assertEqual(expected, actual)
