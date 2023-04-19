import random
# TODO 
# WRITE A FUNCTION THAT WILL RANDOMLY GUESS NUMBERS WITHIN A RANGE
# WRITE A FUNCTION THAT WILL CHECK THE USER INPUT WITH THE GUESSED NUMBER
# COLLECT INPUT FROM USERS
number = value = random.randint(1, 100)

def check_numbers(user_number, number):
    print(number)
    if number == user_number :
        global CORRECT
        CORRECT = False
        return "You win"
    elif number > user_number:
        return "To Low"
    else:
        return "Too High"

print("Welcome to the Guessing game")
difficulty = 0
if input("Select difficulty 'Easy' or 'Hard' ").lower() == "easy":
    difficulty = 9
elif input("Select difficulty 'Easy' or 'Hard' ").lower() == "hard":
    difficulty = 4
else:
    print("Invalid Input")
 
CORRECT = True
while CORRECT == True and difficulty > 0:
    user_number = int(input("Guess a number: "))
    output = check_numbers(user_number,number)
    print(output)