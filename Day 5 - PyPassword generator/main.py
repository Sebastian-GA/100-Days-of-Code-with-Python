# Day 5 - PyPassword generator
# This program generates a random password. The user can select how many
# letters, numbers and symbols are in the password.

# Important!! I don't recommend to use this program for real passwords
# If you want a better password. Use programs like LastPass or 1Password

import random

letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("1234567890")
symbols = list("!#$%&()*+")
chars = [letters, numbers, symbols]

print("Welcome to the PyPassword generator!")
num_letters = abs(int(input("How many letters would you like in your password? ")))
num_numbers = abs(int(input("How many numbers would you like in your password? ")))
num_symbols = abs(int(input("How many symbols would you like in your password? ")))
options = [num_letters, num_numbers, num_symbols]

password = ""

for n in range(sum(options)):
    char_type_to_add = random.randint(0, 2)
    if options[char_type_to_add] > 0:
        options[char_type_to_add] -= 1  # Subtrac items to add of that type of character
    else:
        while not options[char_type_to_add] > 0:
            char_type_to_add = random.randint(0, 2)

    password += chars[char_type_to_add][random.randint(0, len(chars[char_type_to_add]) - 1)]

print(f"Your password is {password}")