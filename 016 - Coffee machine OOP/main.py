from table2ascii import table2ascii, Alignment, PresetStyle
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_module = Menu()
coffee_machine = CoffeeMaker()
money_module = MoneyMachine()


def print_menu(menu):

    _ = menu.get_items()
    _ = _.split("/")
    _.pop()

    drinks = []

    for item in _:
        drink = menu.find_drink(item)
        drinks.append([drink.name, str(drink.cost)])

    menu_list = table2ascii(header=["Product", "Price"],
                            body=drinks,
                            first_col_heading=True,
                            column_widths=[15]+[8],
                            alignments=[Alignment.LEFT] + [Alignment.RIGHT],
                            style=PresetStyle.ascii_compact
                            )
    print(menu_list)


turn_off = False
while not turn_off:
    print("List of products:")
    print_menu(menu_module)

    # Choose a drink
    chosen_drink = None
    while chosen_drink is None:
        chosen_drink = input("What would you like? ({}): ".format(menu_module.get_items())).lower()
        if chosen_drink == "off":
            print("The coffee machine is turning off.")
            turn_off = True
            chosen_drink = None
            break
        elif chosen_drink == "report":
            coffee_machine.report()
            money_module.report()

            chosen_drink = None
            break
        else:
            chosen_drink = menu_module.find_drink(chosen_drink)

    if chosen_drink is None:
        input("Press enter key to continue")
        print()
        print()
        print()
        continue

    # Check the resources
    if coffee_machine.is_resource_sufficient(chosen_drink) is False:
        print("Sorry. Choose another drink")
        input("Press enter key to continue")
        print()
        print()
        print()
        continue

    # Make payment
    if money_module.make_payment(chosen_drink.cost) is False:
        input("Press enter key to continue")
        print()
        print()
        print()
        continue

    # Make the drink
    coffee_machine.make_coffee(chosen_drink)
    input("Press enter to continue")
    print()
    print()
    print()
