from art import vs
from data import data
import random

score = 0


def generate():
    return random.choice(data)


def check(responce,A,B):
    
    if responce == "a":
        if A["follower_count"] > B["follower_count"]:
            return True
        else:
            return False
        # return score + 1
    elif responce == "b":
        if B["follower_count"] > A["follower_count"]:
            return True
        else:
            return False
        # return score + 1
    else:
        print("Invalid input")

B = generate()
res = True
while res == True:
    A = B
    B = generate()
    if A["follower_count"] == B["follower_count"]:
        B = generate()
    name = A["name"]
    print(f"{name}")
    print(vs)
    print(B["name"])
    print(A["follower_count"])
    print(B["follower_count"])

    responce = input("Who has more followers? Type 'A' or 'B': ").lower()
    print(check(responce,A,B))
    if check(responce,A,B) == True:
        score += 1
    else:
        res = False
    print(score)


# print(score)

# print(generate())