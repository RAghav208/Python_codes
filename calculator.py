def addition(a, b):
    return a + b


def substraction(a, b):
    return a - b


def division(a, b):
    return a / b


def multiplication(a, b):
    return a * b


def ig(a, b, c):
    if c == "+":
        print("sum is: ", addition(a, b))
    elif c == "-":
        print("Substraction is: ", substraction(a, b))
    elif c == "/":
        print("division is: ", division(a, b))
    elif c == "*":
        print("multiplication is: ", multiplication(a, b))


c = input("Enter the operator to use:")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

ig(a, b, c)
