# Day 10 - Calculator

def is_number(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def input_number(string):
    num = float(input(string))
    while not is_number(num):
        print("Error: Invalid Input")
        num = float(input(string))
    return num

def input_option(string, options):
    option = input(string).lower()
    while not option in options:
        print("Error: Invalid Input. Choose one option")
        option = input(string).lower()
    return  option

def calculate(a, b, operation):
    if operation == "+":
        result = a + b
    elif operation == "-":
        result = a - b
    elif operation == "*":
        result = a * b
    elif operation == "/" and b != 0:
        result = a / b
    print(f"{a} {operation} {b} = {result}")
    return result

def input_calculation():
    num_a = input_number("Insert the first number: ")
    operation = input_option('What operation do you want to do? ("+", "-", "*" or "/"): ', list("+-*/"))
    num_b = input_number("Insert the second number: ")
    
    if operation == "/" and num_b == 0:
        print("error: Zero Division")
        return "error"
    
    result = calculate(num_a, num_b, operation)
    return result

ans = "null"

while True:
    ans = input_calculation()
    if ans == "error":
        break
    again = input_option('Would you like to continue? Type "yes" or "no": ', ["yes", "no"])
    if again == "no":
        break