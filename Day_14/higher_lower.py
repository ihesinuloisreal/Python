from art import vs
from data import data
import random

score = 0


def generate():
    return random.choice(data)
A = 0
B = 0
for _ in range(1):
    A = generate()
    B = generate()
def check(responce):
    global score
    global A
    global B
    if responce == "a":
        if A["follower_count"] > B["follower_count"]:
            A = A
            return True
        else:
            return False
        # return score + 1
    elif responce == "b":
        if B["follower_count"] > A["follower_count"]:
            A = B
            return True
        else:
            return False
        # return score + 1
    else:
        print("Invalid input")


def run():
    name = A["name"]
    print(f"{name}")
    print(vs)
    print(B["name"])
    print(A["follower_count"])
    print(B["follower_count"])


res = True
while res == True:
    run()
    responce = input("Who has more followers? Type 'A' or 'B': ").lower()
    print(check(responce))
    if check(responce) == True:
        B = generate()
    # elif check(responce) != True:
    #     res = False

#     # print(responce)
#     if check(responce) != True:
#         res = False
#     #     A["follower_count"] = B["follower_count"]
#     #     B = generate()["follower_count"]
#     #     print(B)
#     # print(score)
# answer = check(responce)
# print(answer)

# run()

# print(score)

# print(generate())