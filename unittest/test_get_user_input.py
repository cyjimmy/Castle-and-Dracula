import io
from unittest import TestCase
from game import get_user_input
from unittest.mock import patch


class TestGetUserInput(TestCase):

    @patch('builtins.input', return_value="1")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_list_with_one_element(self, mock_output, _):
        question = "Which color do you like?"
        options = ["Black"]
        actual = get_user_input(question, options)
        expected = "Black"
        self.assertEqual(expected, actual)
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\nWhich color do you like?\n" \
                          "1 Black\n"
        self.assertEqual(expected_output, the_function_printed_this)

    @patch('builtins.input', return_value="3")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_list_with_multiple_elements(self, mock_output, _):
        question = "Which color do you like?"
        options = ["Black", "White", "Blue"]
        actual = get_user_input(question, options)
        expected = "Blue"
        self.assertEqual(actual, expected)
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\nWhich color do you like?\n" \
                          "1 Black\n2 White\n3 Blue\n"
        self.assertEqual(expected_output, the_function_printed_this)

    @patch('builtins.input', return_value="   2   ")
    def test_input_with_whitespace(self, _):
        question = "Which color do you like?"
        options = ["Black", "White", "Blue"]
        actual = get_user_input(question, options)
        expected = "White"
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["9", "1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_input(self, mock_output, _):
        question = "Which color do you like?"
        options = ["Black", "White", "Blue"]
        actual = get_user_input(question, options)
        expected = "Black"
        self.assertEqual(expected, actual)
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\nWhich color do you like?\n" \
                          "1 Black\n2 White\n3 Blue\n" \
                          "That is not a valid option. Please only enter the number shown in the list.\n" \
                          "\nWhich color do you like?\n" \
                          "1 Black\n2 White\n3 Blue\n"
        self.assertEqual(expected_output, the_function_printed_this)

    @patch('builtins.input', return_value="1")
    def test_list_unchanged(self, _):
        question = "Which color do you like?"
        options = ["Black", "White", "Blue"]
        original_options = ["Black", "White", "Blue"]
        get_user_input(question, options)
        self.assertEqual(options, original_options)
