from art import logo
import os

def add(input1,input2):
    return input1 + input2

def sub(input1,input2):
    return input1 - input2

def mul(input1,input2):
    return input1 * input2

def div(input1,input2):
    return input1 / input2

operations = {
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}

print(logo)

def calculator():
    input1 = float(input("What's the first number?: "))
    for operation in operations:
        print(operation)

    continue_calc = True
    while continue_calc:
        operation = input("Pick an operation: ")
        input2 = float(input("What's the next number?: "))
        symbol = operations[operation]
        result = symbol(input1,input2)
        user_input = input(f'Type "y" if you want to continue calculation with {result} or "n" to start a new calculation: ')
        if user_input == 'y':
            input1 = result
            continue_calc
        elif user_input == 'n':
            os.system('clear')
            print(logo)
            calculator()

    if operation == "+":
        add()
    elif operation == "-":
        sub()
    elif operation == "*":
        mul()
    elif operation == "/":
        div()

calculator()


