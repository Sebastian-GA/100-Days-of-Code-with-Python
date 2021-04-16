# Day 12 - Number guessing

import random


def compare(numA, numB):
    """
    numA: Correct number / numB: number guessed
    """
    if numA == numB:
        print("You got it! The answer was {}".format(numA))
        return True
    elif numA > numB:
        print("Too low")
        return False
    else:
        print("Too high")
        return False


def is_number(num):
    """return true if num is a number"""
    try:
        float(num)
        return True
    except ValueError:
        return False


def input_number(string):
    num = input(string)
    while not is_number(num):
        print("Error: Invalid Input")
        num = input(string)
    return num


def input_option(string, options):
    option = input(string).lower()
    while option not in options:
        print("Error: Invalid Input. Choose one option")
        option = input(string).lower()
    return option


if __name__ == "__main__":
    while True:
        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100")
        number = random.randint(1, 100)
        difficulty = input_option("Choose a difficulty. Type 'easy' or 'hard': ", ["easy", "hard"])

        if difficulty == "easy":
            attempts = 10
        else:
            attempts = 5

        for i in range(1, attempts + 1):
            guess = int(input_number("Make a guess: "))
            if compare(number, guess):
                print()
                break
            else:
                if attempts - i > 0:
                    print("Guess again")
                print("You have {} attempts remaining to guess the number.".format(attempts - i))
                if attempts - i == 0:
                    print("You've run out of guesses, you lose.")
                    break

        print()
        if input_option("Do you want to try again?. Type 'yes' or 'no': ", ["yes", "no"]) == "no":
            print("Bye :)")
            break
        else:
            print()
            print()
            print("------------------------------------------------")
