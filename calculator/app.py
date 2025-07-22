import sys

def add(a=0, b=0):
    return a + b

def sub(a=0, b=0):
    return a - b

def multi(a=0, b=0):
    return a * b

def div(a=0, b=0):
    return a / b


def calculator():
    print('1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Exit')

    operation = int(input("What operation do you want to do ? \n") or False)

    if not operation:
        return print("You did not enter an operation. Please enter an operation.")
    if operation == 5:
        return sys.exit(0)

    numberInput1 = int(input("Enter Number 1: "))
    numberInput2 = int(input("Enter Number 2: "))

    match operation:
        case 1:
            print(add(numberInput1, numberInput2))
        case 2:
            print(add(numberInput1, numberInput2))
        case 3:
            print(add(numberInput1, numberInput2))
        case 4:
            print(add(numberInput1, numberInput2))
        case _:
            print("Something went wrong in the calculator.")
            sys.exit(0)

calculator()