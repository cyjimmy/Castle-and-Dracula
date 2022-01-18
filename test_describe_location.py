import io
from unittest import TestCase
from unittest.mock import patch
from game import describe_location


class TestDescribeLocation(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_location_C(self, mock_output):
        location = "C"
        describe_location(location)
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\nYou came across a church that was decorated with colorful stained glass.\n"
        self.assertEqual(expected_output, the_function_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_location_T(self, mock_output):
        location = "T"
        describe_location(location)
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\nYou found an ancient ruin. You felt lucky at the moment, " \
                          "so you started searching the area.\n"
        self.assertEqual(expected_output, the_function_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_location_M(self, mock_output):
        location = "M"
        describe_location(location)
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\nYou found a monster lair. There was a sleeping Cyclops. " \
                          "Out of curiosity, you poked the Cyclops.\n"
        self.assertEqual(expected_output, the_function_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_location_D(self, mock_output):
        location = "D"
        describe_location(location)
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\nYou have finally reached the castle. Dracula is sitting in the hall and looking at you. " \
                          "It is as if he has been expecting you. He sneers and says \"Let's start, shall we?\"\n"
        self.assertEqual(expected_output, the_function_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', return_value=10)
    def test_location_dot_random_number_less_than_equals_to_10(self, _, mock_output):
        location = "."
        describe_location(location)
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\nYou found a lake. It is so calm and clear. You stopped and took a little rest.\n"
        self.assertEqual(expected_output, the_function_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', return_value=35)
    def test_location_dot_random_number_less_than_equals_to_40_larger_than_10(self, _, mock_output):
        location = "."
        describe_location(location)
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\nYou walked into the woods. You feel like you are being watched.\n"
        self.assertEqual(expected_output, the_function_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', return_value=55)
    def test_location_dot_random_number_larger_than_40(self, _, mock_output):
        location = "."
        describe_location(location)
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\nYou are in the forest.\n"
        self.assertEqual(expected_output, the_function_printed_this)
