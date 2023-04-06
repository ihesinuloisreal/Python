word_list = ['word', 'home', 'frank']

import random

choosen_word = random.choice(word_list)
print(choosen_word)
display = []
word_length = len(choosen_word)
for _ in range(word_length):
    display += "_"
print(display)
end_of_game = False

while not end_of_game :
    guess = input("Guess a number: ").lower()

    for position in range(word_length):
        leters = choosen_word[position]
        if leters == guess:
            display[position] = leters
        
    print(display)
    if "_" not in display:
        end_of_game = True
        print("You win.")