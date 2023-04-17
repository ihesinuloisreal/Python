def add(n1, n2):
    """Takes two numbers and add them together"""
    return n1 + n2

def subtraction(n1, n2):
    """Takes two numbers and perform subtraction"""
    return n1 - n2

def multiplication(n1, n2):
    """Takes two numbers and perform multiply"""
    return n1 * n2

def divide(n1, n2):
    """Takes two numbers and perform division"""
    return n1 / n2

operations = {
    "+": add,
    "-": subtraction,
    "*": multiplication,
    "/": divide
}

num1 = int(input("What's the first number? "))
num2 = int(input("What's the second number? "))
for key in operations:
    print(key)

symbol = input("Pick an operation from the line above: ")

outcome = operations[symbol]
first_answer = outcome(num1,num2)
print(f"{num1} {symbol} {num2} = {first_answer}")


response = True

while response == True:
    symbol = input("Pick an operation from the line above: ")
    num3 = int(input("What's the next number? "))
    outcome = operations[symbol]
    second_answer = outcome(outcome(num1,num2), num3)
    print(f"{first_answer} {symbol} {num3} = {second_answer}")
    res = input("Do you want to perform another calculation: Y or N? ").lower()
    if res == "n":
        response = False