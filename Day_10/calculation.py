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
def calculator():
    num1 = float(input("What's the first number? "))
    for key in operations:
        print(key)
    # symbol = input("Pick an operation from the line above: ")
    response = True

    while response == True:
        symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the next number? "))
        outcome = operations[symbol]
        answer = outcome(num1, num2)
        print(f"{num1} {symbol} {num2} = {answer}")  
        res = input("Do you want to perform another calculation: Y or N? ").lower()
        if res == "y":
            num1 = answer
        else:
            response = False
            calculator()

calculator()