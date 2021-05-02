# Day 15 - Coffee machine

import os


def clear():
    os.system('cls')


def is_number(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


def input_option(string, options):
    option = input(string).lower()
    while option not in options:
        print("Error: Invalid Input. Choose one option")
        option = input(string).lower()
    return option


def input_number(string):
    num = input(string)
    while not is_number(num):
        print("Error: Invalid input.")
        num = input(string)
    return int(num)


def insert_coins():
    money = 0
    print("Please insert coins. Old coins only!")
    money += input_number("How many coins of 50?: ") * 50
    money += input_number("How many coins of 100?: ") * 100
    money += input_number("How many coins of 200?: ") * 200
    money += input_number("How many coins of 500?: ") * 500
    money += input_number("How many coins of 1000?: ") * 1000

    print("---------------------")
    print(f"Total money inserted: ${money}")
    return money


products = {
    "espresso": {
        "price": 1000,
        "water": 50,
        "coffee": 18,
        "milk": 0,
     },
    "latte": {
        "price": 1500,
        "water": 200,
        "coffee": 24,
        "milk": 150,
    },
    "cappuccino": {
        "price": 2000,
        "water": 250,
        "coffee": 24,
        "milk": 100,
    },
}

resources = {
    "water": 300,
    "coffee": 100,
    "milk": 200,

}
total_money = 0


def report():
    print("---------------------")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: {total_money}")


def coffee_machine():
    # Choose a product
    print("List of Products:")
    print("Product       |Price")
    for product in products:
        # Convert strings to an specific length
        price = str(products[product]["price"])
        _price = ""
        for _ in range(5 - len(price)):
            _price += " "
        price = _price + price

        while len(product) < 13:
            product += " "

        print("{} | {}".format(product.capitalize(), price))
    print("---------------------")
    product = input_option("What would you like?: ", ["espresso", "latte", "cappuccino", "report"])

    if product == "report":
        report()
        input("Press enter to continue")
        return

    # Insert coins
    money = insert_coins()
    if money < products[product]["price"]:
        print("Sorry, that's not enough money. Money refunded")
        input("Press enter to continue")
        return

    # Check resources
    for item in resources:
        if resources[item] < products[product][item]:
            print(f"Sorry, at the moment there is not enough {item} in the machine")
            print("Money refunded")
            input("Press enter to continue")
            return
    for item in resources:
        resources[item] -= products[product][item]

    # Finish
    global total_money
    total_money += money
    change = money - products[product]["price"]
    if change > 0:
        print(f"Here is ${change} in change")
    print(f"Here is your {product}. Enjoy!")
    print("---------------------")
    input("Press enter to continue")
    return


if __name__ == "__main__":
    while True:
        clear()
        coffee_machine()
