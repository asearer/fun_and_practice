# generates a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
import random

def main():
    print("I'm thinking of a number between 1 and 9 (including 1 and 9).")
    number = random.randint(1, 9)
    guess = int(input("Guess the number: "))
    if guess == number:
        print("You guessed correctly!")
    else:
        print("Nope. The number I was thinking of was", number)
        