# Day 7 - Hangman

import random
from ascii_art import ascii_hangman, hangman_title
from words import words_list
import os
def clear(): os.system('cls')  # Clear terminal on windows

def finished():
    if "".join(user_word) == word:
        print("You win")
        return True
    elif lives == 0:
        print("You lose")
        print(f"The word was {word}")
        return True
    else:
        return False

def print_hangman():
    # print(f"Your score {lives}")
    print(ascii_hangman[lives])


# Configuration
word = random.choice(words_list).lower()

user_word = []
for n in range(len(word)):
    user_word.append("_")

lives = 6
letter = ""
used_letters = []  # Letters that have been entered

# Game
clear()
print("Welcome to")
print(hangman_title)

while not finished():
    letter = input("Guess a letter: ").lower()
    # Check input
    while len(letter) != 1 or letter in "1234567890!\"#$%&/()=?¿'*+-_]}[{^;,:.":
        print("error: Incorrect input. The input must be a letter.")
        letter = input("Try again. Guess a letter: ").lower()
    clear()

    # Check letter
    if letter in word and letter not in user_word:
        used_letters.append(letter)
        # Replace that letter in 'user_word'
        for n in range(len(word)):
            if letter == word[n]:
                user_word[n] = letter
    
    elif letter in user_word:
        print("You have already guessed that letter. Try another letter.")

    elif letter in used_letters:
        print("You have already entered that letter. Try another letter.")

    else:
        used_letters.append(letter)
        #Lose lives
        lives -= 1
        print(f"You guessed {letter}, that's not in the word. You lose a life.")

    # Print hangman and word
    print_hangman()
    print(" ".join(user_word))

