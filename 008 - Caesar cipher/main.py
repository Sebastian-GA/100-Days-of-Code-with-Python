# Day 8 - Caesar cipher
from ascii_art import title

# Configuration
alphabet = list("abcdefghijklmnopqrstuvwxyz")
numbers = list("0123456789")

# Data input
print(title)
print("Select an option:")
print("1. Encode a message")
print("2. Decode a message")
option = input()
while option != "1" and option != "2":
    print("error. Select one of the given options")
    option = input()

check_input = False
while not check_input:
    message = list(input("Type your message. (only letters, numbers and spaces): ").lower())
    for n in range(len(message)):
        if message[n] not in alphabet and message[n] not in numbers and message[n] != " ":  # Allows spaces
            print("error. The message must include only letters.")
            break
        elif n == len(message) - 1:
            check_input = True
            break
shift = abs(int(input("Type the shift number: ")))
shift = shift % len(alphabet)
if option == "2":
    shift *= -1

# Calculating result
final_message = ""
for char in message:
    if char in alphabet:
        position = alphabet.index(char)
        new_position = (position + shift) % len(alphabet)
        final_message += alphabet[new_position]
    elif char in numbers:
        position = numbers.index(char)
        new_position = (position + shift) % len(numbers)
        final_message += numbers[new_position]
    elif char == " ":
        final_message += " "
        continue

# Print result
if option == "1":
    print(f"Your message encoded is: {final_message}")
else:
    print(f"Your message decoded is: {final_message}")
