
# Day 11 - Blackjack

import random
import os
from ascii_art import logo, ascii_card


def clear(): os.system('cls')


def is_number(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


def input_option(string, options):
    option = input(string).lower()
    while option not in options:
        print("Error: Invalid Input. Choose one option")
        option = input(string).lower()
    return option


def card_value(card):
    if is_number(card):
        return int(card)
    else:
        if card in ["K", "Q", "J"]:
            return 10
        else:
            return [1, 11]


def choose_card():
    card = [0]
    suit = 0
    value = 0
    while card[0] == 0:  # If the card has been used
        suit = random.randint(0, 3)
        value = random.randint(0, 12)
        card = [deck[suit][value], suit]

    deck[suit][value] = 0  # That card cannot be used again
    return card


def sum_cards(cards_in_hand):
    values = []
    for card in cards_in_hand:
        values.append(card_value(card[0]))
    
    # Simplify list of values
    temp_values = [0]
    for value in values:
        if type(value) == int:
            temp_values[0] += value
        else:
            temp_values.append(value)
    values = temp_values
    
    # Sum first and second values
    while len(values) > 1:
        temp_values = []
        if type(values[0]) == int:
            for i in values[1]:
                temp_values.append(values[0] + i)
        else:
            for i in values[0]:
                for j in values[1]:
                    temp_values.append(i + j)
        
        values[0] = temp_values
        del values[1]
    
    values = values[0]
    if type(values) != list:
        values = [values]
    values = list(set(values))  # Remove duplicates
    return values


def print_cards(cards_in_hand, hide_first_card):
    temp_cards_in_hand = []
    temp_cards_in_hand.extend(cards_in_hand)
    if hide_first_card:
        temp_cards_in_hand[0][0] = "?"
    for row in range(5):
        row_str = ""
        for card in temp_cards_in_hand:
            row_str += ascii_card(card[1], card[0])[row]
        print(row_str)


# Setup
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "K", "Q", "J"]
deck = [cards, cards, cards, cards]

# Game
clear()
print(logo)
while input_option('Do you want to play a game of Blackjack? Type "yes" or "no": ', ["yes", "no"]) == "yes":
    clear()
    # Reset deck
    deck = [cards, cards, cards, cards]

    # Reset cards
    user_cards = []
    computer_cards = []

    for i in range(2):
        user_cards.append(choose_card())
        computer_cards.append(choose_card())

    # Print cards
    print(f"Your cards are:")
    print_cards(user_cards, False)
    print(f"Computer's cards are:")
    print_cards(computer_cards, True)
    
    while min(sum_cards(user_cards)) < 21 and input_option('Do you want another card? Type "yes" or "no": ', ["yes", "no"]) == "yes":
        clear()
        user_cards.append(choose_card())
        print(f"Your cards are:")
        print_cards(user_cards, False)
        print(f"Computer's cards are:")
        print_cards(computer_cards, True)

    if max(sum_cards(computer_cards)) < 17:
        clear()
        print(f"Your final cards are:")
        print_cards(user_cards, False)
        print(f"Computer's cards are:")
        print_cards(computer_cards, False)
        
        # Add cards to computer until the sum of them are greater than 17
        while max(sum_cards(computer_cards)) < 17:
            print("As computer has cards that sums less than 17 it takes 1 card")
            computer_cards.append(choose_card())
            print(f"Computer's cards are:")
            print_cards(computer_cards, False)

    # Print final cards
    sum_cards_user = sum_cards(user_cards)
    sum_cards_computer = sum_cards(computer_cards)
    clear()
    print(f"Your final cards are:")
    print_cards(user_cards, False)
    print(f"Computer's final cards are:")
    print_cards(computer_cards, False)

    # Compare sums
    if min(sum_cards_user) > 21 and min(sum_cards_computer) > 21:
        print("Computer and user went over")
    elif min(sum_cards_user) > 21:
        print("You went over. Computer wins")
    elif min(sum_cards_computer) > 21:
        print("Computer went over. You win")
    else:

        # Remove all sums that are greater than 21
        temp_sum = []
        for value in sum_cards_user:
            if value <= 21:
                temp_sum.append(value)
        sum_cards_user = temp_sum
        temp_sum = []
        for value in sum_cards_computer:
            if value <= 21:
                temp_sum.append(value)
        sum_cards_computer = temp_sum
        
        # Check winner
        if max(sum_cards_user) == max(sum_cards_computer):
            print("It's a draw")
        elif max(sum_cards_user) > max(sum_cards_computer):
            print("You win")
        elif max(sum_cards_user) < max(sum_cards_computer):
            print("You lose")
