from art import vs
from data import data
import random

score = 0


def generate():
    return random.choice(data)

A = generate()
B = generate()
def check(responce):
    global score
    if responce == "a":
        value = str(A["follower_count"]) > str(B["follower_count"])
        score += 1
        return value
    else:
        value = str(A["follower_count"]) < str(B["follower_count"])
        score += 1
        return value

def run():
    global A
    global B
    name = A["name"]
    print(f"{name}")
    print(vs)
    print(B["name"])
    print(A["follower_count"])
    print(B["follower_count"])
    
run()
# responce = input("Who has more followers? Type 'A' or 'B': ").lower()
res = True
while res == True:
    run()
    responce = input("Who has more followers? Type 'A' or 'B': ").lower()


    # print(responce)
    if check(responce) != True:
        res = False
    #     A["follower_count"] = B["follower_count"]
    #     B = generate()["follower_count"]
    #     print(B)
    # print(score)
answer = check(responce)
print(answer)

run()

# print(score)

# print(generate())