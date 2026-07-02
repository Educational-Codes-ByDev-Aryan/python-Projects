import itertools
# itertools is a standard Python library that gives you tools
#  to work with loops and sequences more efficiently.
symbol = ["X", "/", "-", "+", "%", "x^3"]

for i in itertools.count(1):
    # here i just holds the current value

    # user input
    number1 = int(input("Enter the number : "))
    symbol = input("Enter the operation : ")
    number2 = int(input("Enter the number : "))


    # conditions
    if symbol == "x":
        print(f"{number1} {symbol} {number2} =", number1 * number2)
    elif symbol == "/":
        print(f"{number1} {symbol} {number2} =", number1 / number2)
    elif symbol == "+":
        print(f"{number1} {symbol} {number2} =", number1 + number2)
    elif symbol == "-":
        print(f"{number1} {symbol} {number2} =", number1 - number2)
    elif symbol == "%":
        print(f"{number1} {symbol} {number2} =", number1 % number2)
    elif symbol == "x^3":
        print(f"{number1} {symbol} {number2} =", number1 * number2 * number1)
