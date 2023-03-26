import random
# ******Game Rules******

# Rock wins against Scissors
# Scissors wins against Paper
# Paper wins against Rock

Rock = "Rock"
Scissors = "Scissors"
Paper = "Paper"

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

Schoice = random.randint(0, 2)

print()

if choice == 0:
    if Schoice == 1:
        print("You Win")
    else:
        print("You Lose")


elif choice == 1:
    if Schoice == 2:
        print("You Win")
    else:
        print("You Lose")
elif choice == 2:
    if Schoice == 1:
        print("You Win")
    else:
        print("You Lose")