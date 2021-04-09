# Day 11 - Blackjack

import random
import os
from ascii_art import logo

def clear(): os.system('cls')

def is_number(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

def input_option(string, options):
    option = input(string).lower()
    while not option in options:
        print("Error: Invalid Input. Choose one option")
        option = input(string).lower()
    return  option


def card_value(card):
    if is_number(card):
        return int(card)
    else:
        if card in ["K", "Q", "J"]:
            return 10
        else:
            # return [1, 11]
            return 1  # This is temporal

def choose_card(deck):
    card = 0
    while card == 0:  # If the card has been used
        color = random.randint(0, 3)
        value = random.randint(0, 13)
        card = deck[color][value]
    
    deck[color][value] = 0  # That card cannot be used again
    return card

def sum_cards(cards):
    sum = 0
    for card in cards:
        sum += card_value(card)
    return sum

def print_cards(cards, hide_first_card):  # I want to update this later!
    if not hide_first_card:
        return ", ".join(cards)
    else:
        cards[0] = "?"
        return ", ".join(cards)


# Game
def play_blackjack():
    print(logo)
    
    # Setup
    cards = ["A", "1", "2", "3", "4", "5", "6", "7", "8" , "9", "10", "K", "Q", "J"]
    deck = [cards, cards, cards, cards]

    # Reset cards
    user_cards = []
    computer_cards = []

    for i in range(2):
        user_cards.append(choose_card(deck))
        computer_cards.append(choose_card(deck))

    # Print cards
    print(f"Your cards are: {print_cards(user_cards, False)}")
    print(f"Computer's cards are: {print_cards(computer_cards, True)}")
    print(f"{sum_cards(computer_cards)} || {sum_cards(user_cards)}")  # Temporal
    
    while sum_cards(user_cards) <= 21 and input_option('Do you want another card? Type "yes" or "no": ', ["yes", "no"]) == "yes":
        user_cards.append(choose_card(deck))
        print(f"Your cards are: {print_cards(user_cards, False)}")
        print(f"Computer's cards are: {print_cards(computer_cards, True)}")
        print(f"{sum_cards(computer_cards)} || {sum_cards(user_cards)}")  # Temporal

    
    
    a = input()  # Wait!!
    # Compare sums


while input_option('Do you want to play a game of Blackjack? Type "yes" or "no": ', ["yes", "no"]) == "yes":
    clear()
    play_blackjack()
