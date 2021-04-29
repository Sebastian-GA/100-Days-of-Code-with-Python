# Day 14 - Higher Lower Game

from ascii_art import logo, vs
from game_data import data
from random import shuffle
import os


def clear(): os.system('cls')


def input_option(string, options):
    option = input(string).lower()
    while option not in options:
        print("Error: Invalid Input. Choose one option")
        option = input(string).lower()
    return option


while True:
    clear()
    print(logo)

    # Setup
    should_continue = True
    score = 0
    shuffle(data)

    # Start game
    while should_continue:
        if score + 1 > len(data):
            print("Wow! You have reached the maximum score")
            print(f"Your final score: {score}")
            break

        print("A")
        print("{}, a {}, from {}".format(data[score]["name"], data[score]["description"], data[score]["country"]))
        print("Number of followers: {}M".format(data[score]["follower_count"]))

        print(vs)

        print("B")
        print("{}, a {}, from {}".format(data[score + 1]["name"], data[score + 1]["description"], data[score + 1]["country"]))

        choice = input_option("Who has more followers? Type 'A' or 'B': ", ["a", "b"])
        print()
        print()
        print("-----------------------------------------------")
        print()
        print()

        if data[score]["follower_count"] == data[score + 1]["follower_count"]:
            score += 1
            print("You are right. Current score: {}".format(score))
        elif data[score]["follower_count"] > data[score + 1]["follower_count"] and choice == "a":
            score += 1
            print("You are right. Current score: {}".format(score))
        elif data[score]["follower_count"] < data[score + 1]["follower_count"] and choice == "b":
            score += 1
            print("You are right. Current score: {}".format(score))
        else:
            # You loose
            print("Sorry. You are wrong. Final score: {}".format(score))
            should_continue = False

    should_continue = input_option("Would you like to play again? Type 'yes' or 'no': ", ["yes", "no"])
    print()
    print()
    print("-----------------------------------------------")
    print()
    print()
    if should_continue == "no":
        break
