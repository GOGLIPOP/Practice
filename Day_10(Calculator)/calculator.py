from art import logo
import os


loop = "yes"


def add(n1,n2):
    return n1 + n2


def substract(n1,n2):
    return n1 - n2


def multiply(n1,n2):
    return n1 * n2


def devide(n1,n2):
    return n1 / n2


def start(n1):
    global loop
    os.system('Cls')

    n2 = int(input("What's the next number? "))

    for i in operation:
        print(i)

    operation_symbol = str(input("What's the operation? "))

    while operation_symbol not in "+-*/":
        operation_symbol = str(input("Error, please choose the operation "))

    else:
        if operation_symbol == '+':
            answer = add(n1, n2)
        elif operation_symbol == '-':
            answer = substract(n1, n2)
        elif operation_symbol == '*':
            answer = multiply(n1, n2)
        elif operation_symbol == '/':
            answer = devide(n1, n2)

    print(f"{n1} {operation_symbol} {n2} = {answer}")
    n1 = answer
    loop = str(input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit... ").lower())


operation = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : devide,
}

print(logo)

n1 = int(input("What's the first number? "))
n2 = int(input("What's the second number? "))

for i in operation:
    print(i)

operation_symbol = str(input("What's the operation? "))

while operation_symbol not in "+-*/":
    operation_symbol = str(input("Error, please choose the operation "))

else:
    if operation_symbol == '+':
        answer = add(n1, n2)
    elif operation_symbol == '-':
        answer = substract(n1, n2)
    elif operation_symbol == '*':
        answer = multiply(n1, n2)
    elif operation_symbol == '/':
        answer = devide(n1, n2)

print(f"{n1} {operation_symbol} {n2} = {answer}")
n1 = answer
loop = str(input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit... ").lower())


while loop != 'no' and loop != 'n':
    if loop == "yes" or loop == 'y':
       start(n1)
    else:
        print(loop)
        loop = str(input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit... ").lower())
else:
    ...


