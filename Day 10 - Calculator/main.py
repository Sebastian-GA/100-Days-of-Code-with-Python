# Day 10 - Calculator

from ascii_art import logo

def is_number(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def input_number(string):
    num = input(string)
    while not is_number(num):
        print("Error: Invalid Input")
        num = input(string)
    return num

def input_number(string, letter_numbers):
    num = input(string).lower()
    while not is_number(num) and not num in letter_numbers:
        print("Error: Invalid Input")
        num = input(string).lower()
    
    # Convert input to a number
    if num in letter_numbers:  # it's a letter_number
        num = letter_numbers[num]
    else:  # it's a number
        num = float(num)
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

def input_calculation(ans):
    valid_numbers = 'You can also use "pi", "e" and "tau"'
    if ans != "null":
        letter_numbers["ans"] = ans
        valid_numbers = 'You can also use "pi", "e", "tau" and "ans"'
    

    num_a = input_number("Insert the first number " + valid_numbers + ": ", letter_numbers)
    operation = input_option('What operation do you want to do? ("+", "-", "*" or "/"): ', list("+-*/"))
    num_b = input_number("Insert the second number " + valid_numbers + ": ", letter_numbers)

    if operation == "/" and num_b == 0:
        print("error: Zero Division")
        return "error"
    
    result = calculate(num_a, num_b, operation)
    return result


# Setup
ans = "null"
letter_numbers = {
    "pi" : 3.141592653589793,
    "e" : 2.718281828459045,
    "tau" : 6.283185307179586,
}

print(logo)
while True:
    ans = input_calculation(ans)
    if ans == "error":
        break
    again = input_option('Would you like to continue? Type "yes" or "no": ', ["yes", "no"])
    if again == "no":
        break
