# basic calculator

"""I will build a simple calcultor. It will calculate addition, subtraction, multiplication, division."""


def addition(a, b):
    return f"{a} + {b}  = {a + b}"

def subtract(a, b):
    return f"{a} - {b} = {a - b}"

def multiply(a, b):
    return f"{a} + {b} = {a * b}"

def division(a, b):
    return f"{a} / {b} = {a / b}"

def get_input():
    a = int(input("Enter your first digit: "))
    b = int(input("Enter Your second digit: "))
    return a, b

while True:
    print("You can choose what opertion doing on it.(Choose Option)")
    print("A. Addtion")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("Q. Quit operation")
    
    operation = str(input("Enter your option:  ")).upper()
    
    if operation == "A":
        print("A. Addition")
        a, b = get_input()
        print(addition(a, b))
    elif operation == "B":
        print("B. Subtraction")
        a, b = get_input()
        print(subtract(a, b))  
    elif operation == "C":
        print("C. multiplication")
        a, b = get_input()
        print(multiply(a, b))   
    elif operation == "D":
        print("D. Division")
        a, b = get_input()
        print(division(a, b))
    elif operation == 'Q':
        quit()
    else:
        print("Not valid option.")