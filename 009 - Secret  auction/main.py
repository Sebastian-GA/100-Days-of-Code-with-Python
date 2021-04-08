# Day  9 - Secret Auction

import os
from ascii_art import logo
def clear(): os.system('cls')  # Clear terminal on windows

# Setup
bidders = {}

print(logo)
print("Welcome to the secret auction")

while True:
    name = input("What's your name? ")
    bid = abs(int(input("What's your bid? $")))

    bidders[name] = bid

    other_bidder = input('Are there any other bidder? Type "yes" or "no" ')
    clear()
    # Only checks if don't type "yes", "Yes" or "YES"
    if other_bidder.lower() != "yes":
        break
    
# Calculate the winner(s)
max_bidders = []
for bidder in bidders:
    if len(max_bidders) == 0:  # First bidder
        max_bidders.append(bidder)
    else:
        if bidders[bidder] > bidders[max_bidders[0]]:  # Compares the bids with one of the bidders who has the max bid
            max_bidders = []
            max_bidders.append(bidder)
        elif bidders[bidder] == bidders[max_bidders[0]]:
            max_bidders.append(bidder)

# Shows the winner(s)
if len(max_bidders) == 1:
    print(f"The winner is {max_bidders[0]} with a bid of ${bidders[max_bidders[0]]}.")
else:
    string_of_winners = ""
    for n in range(len(max_bidders)):
        if n < len(max_bidders) - 2:
            string_of_winners += f"{max_bidders[n]}, "
        elif n == len(max_bidders) - 2:
            string_of_winners += f"{max_bidders[n]} and "
        else:
            string_of_winners += max_bidders[n]
    
    print(f"The winners are {string_of_winners} with a bid of ${bidders[max_bidders[0]]}.")
