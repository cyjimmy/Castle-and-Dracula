import io
from unittest import TestCase
from unittest.mock import patch
from game import get_command


class TestGetCommand(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', return_value="5")
    def test_valid_input(self, _, mock_output):
        actual = get_command()
        expected = "Check Map"
        self.assertEqual(expected, actual)
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\nWhat do you want to do?" \
                          "\n1 Up\n2 Down\n3 Left\n4 Right\n5 Check Map\n6 Check Status\n7 Quit Game\n"
        self.assertEqual(expected_output, the_function_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["100", "2"])
    def test_invalid_input(self, _, mock_output):
        get_command()
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\nWhat do you want to do?" \
                          "\n1 Up\n2 Down\n3 Left\n4 Right\n5 Check Map\n6 Check Status\n7 Quit Game" \
                          "\nThat is not a valid option. Please only enter the number shown in the list.\n" \
                          "\nWhat do you want to do?" \
                          "\n1 Up\n2 Down\n3 Left\n4 Right\n5 Check Map\n6 Check Status\n7 Quit Game\n"
        self.assertEqual(expected_output, the_function_printed_this)
