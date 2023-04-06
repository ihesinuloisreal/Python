word_list = ['word', 'home', 'frank']

import random

choosen_word = random.choice(word_list)
print(choosen_word)
display = []
word_length = len(choosen_word)
for _ in range(word_length):
    display += "_"
print(display)


guess = input("Guess a number: ").lower()

for position in range(word_length):
    leters = choosen_word[position]
    if leters == guess:
        display[position] = leters
    

print(display)