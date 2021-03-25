# Day 7 - Hangman

import random

def finished():
    if "".join(user_word) == word:
        print("You win")
        return True
    elif lives == 0:
        print("You lose")
        return True
    else:
        return False

def print_hangman():
    print(f"Your score {lives}")

# Configuration
words_list = ["horse", "house", "university", "python", "apple", "sausage"]
word = random.choice(words_list)

user_word = []
for n in range(len(word)):
    user_word.append("_")

lives = 10
letter = ""
used_letters = []

# Game
while not finished():
    letter = input("Guess a letter: ")
    # Check input
    while len(letter) != 1 or letter in "1234567890!\"#$%&/()=?¿'*+-_]}[{^;,:.":
        print("error: Incorrect input. The input must be a letter.")
        letter = input("Try again. Guess a letter: ")
    
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

