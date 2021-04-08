# Treasure island
# This is a mini game where you have to take decisions.
# If you're lucky you could get the treasure

print("*******************************************************************************")
print("          |                   |                  |                     |       ")
print(" _________|________________.=""_;=.______________|_____________________|_______")
print("|                   |  ,-\"_,=""     `\"=.|                  |                   ")
print("|___________________|__\"=._o`\"-._        `\"=.______________|___________________")
print("          |                `\"=._o`\"=._      _`\"=._                     |       ")
print(" _________|_____________________:=._o \"=._.\"_.-=\"'\"=.__________________|_______")
print("|                   |    __.--\" , ; `\"=._o.\" ,-\"\"\"-._ \".   |                   ")
print("|___________________|_._\"  ,. .` ` `` ,  `\"-._\"-._   \". '__|___________________")
print("          |           |o`\"=._` , \"` `; .\". ,  \"-._\"-._; ;              |       ")
print(" _________|___________| ;`-.o`\"=._; .\" ` '`.\"\` . \"-._ /_______________|_______")
print("|                   | |o;    `\"-.o`\"=._``  '` \" ,__.--o;   |                   ")
print("|___________________|_| ;     (#) `-.o `\"=.`_.--\"_o.-; ;___|___________________")
print("____/______/______/___|o;._    \"      `\".o|o_.--\"    ;o;____/______/______/____")
print("/______/______/______/_\"=._o--._        ; | ;        ; ;/______/______/______/_")
print("____/______/______/______/__\"=._o--._   ;o|o;     _._;o;____/______/______/____")
print("/______/______/______/______/____\"=._o._; | ;_.--\"o.--\"_/______/______/______/_")
print("____/______/______/______/______/_____\"=.o|o_.--\"\"___/______/______/______/____")
print("/______/______/______/______/______/______/______/______/______/______/_____ /")
print("*******************************************************************************")

print()
print("Welcome to Treasure island")
print("Your mission is to find the treasure. There is only one oportunity. So, don't fail")
print()

left_or_right = input("You're at a cross road. Where do you want to go? " + 'Type "left" or "right" ')
print()

if left_or_right == "left":
    print("You got to a beach. There is an island opposite the beach, but there is a boat comming.")
    swim_or_wait = input("What do you do? " + 'Type "swim"  or "wait" ')
    print()

    if swim_or_wait == "wait":
        print("You got to the island. There are a house, an old bridge and a lake.")
        last_option = input("Where do you go first? " + 'Type "house", "bridge" or "lake" ')
        print()

        if last_option == "house":
            print("Yeah! You got the treasure in the house")
        elif last_option == "bridge":
            print("The bridge was very old and when you tried to pass the bridge fell and you died. Game Over.")
        elif last_option == "lake":
            print("You discovered a mounster in the lake, you tried to get closer and it ate you. Game Over.")
        else:
            print("error. Check your input.")
        
    elif swim_or_wait == "swim":
        print("Who the heck decide to swim in a sea full of sharks. Game Over.")
    else:
        print("error. Check your input.")

elif left_or_right == "right":
    print("You lost in the jungle. The right way was not the right. Game Over.")
else:
    print("error. Check your input.")
