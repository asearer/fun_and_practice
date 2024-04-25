import unittest
from unittest.mock import patch, MagicMock
import random

def main():
    print("I'm thinking of a number between 1 and 9 (including 1 and 9).")
    number = random.randint(1, 9)
    guess = int(input("Guess the number: "))
    if guess == number:
        print("You guessed correctly!")
    else:
        print("Nope. The number I was thinking of was", number)

class TestMainFunction(unittest.TestCase):

    @patch('builtins.print')
    @patch('builtins.input', return_value='5')
    @patch('random.randint', return_value=5)
    def test_correct_guess(self, mock_randint, mock_input, mock_print):
        main()
        mock_print.assert_called_with("You guessed correctly!")

    @patch('builtins.print')
    @patch('builtins.input', return_value='3')
    @patch('random.randint', return_value=5)
    def test_incorrect_guess(self, mock_randint, mock_input, mock_print):
        main()
        mock_print.assert_called_with("Nope. The number I was thinking of was", 5)

if __name__ == "__main__":
    unittest.main()
