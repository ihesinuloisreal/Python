import random

CORRECT = True
# TODO 
# RANDOMLY GUESS NUMBERS WITHIN A RANGE AND SAVE TO A VARIABLE
# WRITE A FUNCTION THAT WILL CHECK THE USER INPUT WITH THE GUESSED NUMBER
# COLLECT INPUT FROM USERS
number = value = random.randint(1, 100)

def check_numbers(user_number, number, turns):
    print(number)
    if number == user_number :
        global CORRECT
        CORRECT = False
        return "You win"
    elif number > user_number:
        print("Too Low")
        return turns - 1
    else:
        print("Too High")
        return turns - 1

def level():
    if input("Choose difficulty. Type 'Easy' or 'Hard': ").lower() == "easy":
        return 10
    else:
        return 5

def game():
    print("Welcome to the Number Guessing game")
    print("I am thinking of a number between 1 to 100")

    turns = level()
    print(f"You have {turns} times left to guess")

    user_number = 0
    while user_number != number:
        user_number = int(input("Guess a number: "))
        turns = check_numbers(user_number,number, turns)
        # print(output)
        print(f"You have {turns} times left to guess")
        if turns == 0:
            print("You run out of guess. You Lose")
            return
        elif user_number != number:
            print("Guess again")

game()