import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(card):
    if sum(card) == 21 and len(card) == 2 :
        return 0
    
    if 11 in card and sum(card) > 21 :
        card.remove(11)
        card.append(1)
        
    return sum(card)

def compare(my_total, computer_total):
    if my_total == computer_total :
        return "Draw"
    elif computer_total == 0:
        return "Lose, opponent has Blackjack "
    elif my_total == 0 :
        return "Win with a Blackjack "
    elif my_total > 21:
        return "You went over. You lose"
    elif computer_total > 21 :
        return "Opponent went over. You win"
    elif my_total > computer_total:
        return "You Win"
    else:
        return "You Lose"


my_card = []
computer_card = []
is_game_over = False
for _ in range(2):
    my_card.append(deal_card())
    computer_card.append(deal_card())

print(my_card)
print(computer_card[0])
while not is_game_over:
    my_total = calculate_score(my_card)
    computer_total = calculate_score(computer_card)
    

    if my_total == 0 or computer_total == 0 or my_total > 21 :
        is_game_over = True
    else:
        res = input("Do you want to draw another card? 'y' or 'n': ")
        if res == "y":
            my_card.append(deal_card())
        else:
            is_game_over = True

while computer_total != 0 and computer_total < 17:
    computer_card.append(deal_card())
    computer_total = calculate_score(computer_card)

print(f"{my_total} {my_card}")
print(f"{computer_total} {computer_card}")
print(compare(my_total, computer_total))