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
        value = random.randint(0, 12)
        card = deck[color][value]
    
    deck[color][value] = 0  # That card cannot be used again
    return card

def sum_cards(cards):
    sum = 0
    for card in cards:
        sum += card_value(card)
    return [sum]  # Temporal

def print_cards(cards, hide_first_card):  # I want to update this later!
    if hide_first_card == False:
        return ", ".join(cards)
    else:
        temp_cards = []  # Why I cannot simply change the first item? if I'm not usig a global variable
        temp_cards.extend(cards)
        temp_cards[0] = "?"
        return ", ".join(temp_cards)


# Game
def play_blackjack():
    print(logo)
    
    # Setup
    cards = ["A", "2", "3", "4", "5", "6", "7", "8" , "9", "10", "K", "Q", "J"]
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
    
    while min(sum_cards(user_cards)) < 21 and input_option('Do you want another card? Type "yes" or "no": ', ["yes", "no"]) == "yes":
        user_cards.append(choose_card(deck))
        print(f"Your cards are: {print_cards(user_cards, False)}")
        print(f"Computer's cards are: {print_cards(computer_cards, True)}")

    if max(sum_cards(computer_cards)) < 17:
        print()
        print("-------------------------------------------------------")
        print(f"Your final cards are: {print_cards(user_cards, False)}")
        print(f"Computer's cards are: {print_cards(computer_cards, False)}")
        
        # Add cards to computer until the sum of them are greater than 17
        while max(sum_cards(computer_cards)) < 17:
            print("As computer has cards that sums less than 17 it takes 1 card")
            computer_cards.append(choose_card(deck))
            print(f"Computer's cards are: {print_cards(computer_cards, False)}")

    # Print final cards
    sum_cards_user = sum_cards(user_cards)
    sum_cards_computer = sum_cards(computer_cards)
    print()
    print("-------------------------------------------------------")
    print(f"Your final cards are: {print_cards(user_cards, False)} that sums these posible values {sum_cards_user}")
    print(f"Computer's final cards are: {print_cards(computer_cards, False)} that sums these posible values {sum_cards_computer}")


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
        for value in sum_cards_computer:
            if value <= 21:
                temp_sum.append(value)
        sum_cards_computer = temp_sum

        if max(sum_cards_user) == max(sum_cards_computer):
            print("It's a draw")
        elif max(sum_cards_user) > max(sum_cards_computer):
            print("You win")
        elif max(sum_cards_user) < max(sum_cards_computer):
            print("You lose")
    

clear()
while input_option('Do you want to play a game of Blackjack? Type "yes" or "no": ', ["yes", "no"]) == "yes":
    clear()
    play_blackjack()
