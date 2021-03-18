# Day 2 - Tip calculator
# This program calculates how much money should each person pay for a dinner

a = 13.946
print(round(a,2))

print("Welcome to the tip calculator")

bill = float(input("What was the total bill? $"))
percent_of_tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

total = bill * (percent_of_tip / 100 + 1)  # tip + bill
money = round(total / people, 2)  # money each person should pay
money = "{:.2f}".format(money)

print(f"Each person should pay ${money}")
