word_list = ['word', 'home', 'frank']

import random

choosen_word = random.choice(word_list)
guess = input("Guess a number: ").lower()

for leters in choosen_word:
    if leters == guess:
        print("Right")
    else: 
        print("Wrong")