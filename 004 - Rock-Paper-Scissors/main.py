# Day 4 - Rock-Paper-Scissors

import random

def print_ASCII(option):
    if option == 0:
        print("    _______                        _______                             _______")
        print("---'   ____)           ___     ---'   ____)____           ____     ---'   ____)____")
        print("      (_____)     \  / |__               ______)     \  / |__                ______)")
        print("      (_____)      \/  ___|              _______)     \/  ___|            __________)")
        print("      (____)                            _______)                         (____)")
        print("---.__(___)                    ---.__________)                     ---.__(___)")
    elif option == 1:
        print("    _______")
        print("---'   ____)")
        print("      (_____)")
        print("      (_____)")
        print("      (____)")
        print("---.__(___)")
    elif option == 2:
        print("    _______")
        print("---'   ____)____")
        print("          ______)")
        print("          _______)")
        print("         _______)")
        print("---.__________)")
    else:
        print("    _______")
        print("---'   ____)____")
        print("          ______)")
        print("       __________)")
        print("      (____)")
        print("---.__(___)")

print("Welcome to Rock-Paper-Scissors")
print_ASCII(0)
print("You will play with the computer. The first with 3 points is the winner.")
print()

score = [0, 0]  # [0]: Player // [1]: Computer

while True:
    player_option = int(input("What do you choose? Type 1 for Rock, 2 for Paper or 3 for Scissors. "))
    while 3 < player_option or player_option < 1:
        print("error. Check your input and try again.")
        player_option = int(input("What do you choose? Type 1 for Rock, 2 for Paper or 3 for Scissors. "))
    
    computer_option = random.randint(1, 3)

    print("Your choice:")
    print_ASCII(player_option)
    print()
    print("Computer choice:")
    print_ASCII(computer_option)
    print()

    if player_option == computer_option:
        print("It's a draw.")
    elif (player_option == 1 and computer_option == 3) or (player_option == 2 and computer_option == 1) or (player_option == 3 and computer_option == 2):
        print("You won.")
        score[0] += 1
    else:
        print("Computer won.")
        score[1] += 1

    print("New score:")
    print(f"You: {score[0]} | Computer: {score[1]}")
    if score[0] == 3:
        print("You has won the match.")
        break
    elif score[1] == 3:
        print("Computer has won the match. Game Over")
        break

    print()
