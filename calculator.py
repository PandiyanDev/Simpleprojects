# what is the operation doing

def calculte():
    operation = str(input("""
    Enter the math operation like
    +  for addition
    - for substraction
    x for multiplication
    / for division :   """))

    a = int(input("Enter a first number: "))
    b = int(input("Enter the second number : "))
    
    if operation == '+':
        result = a + b
        print(f'{a} + {b} = {result}')
    elif operation == '-':
        result = a - b
        print(f'{a} - {b} = {result}')
    elif operation == 'x':
        result = a * b
        print(f'{a} * {b} = {result}')
    elif operation == '/':
        result = a / b
        print(f'{a} / {b} = {result}')
    else:
        print('You have not type any number. So run again')

    repeat_calculate()

def repeat_calculate():
    repeat = input('Do you want calculate more. If yes means type  "y"  or no means type "n":  ')

    if repeat.upper() == 'Y':
        calculte()
    else:
        print('Thank you for use it and see you later.')

calculte()


    