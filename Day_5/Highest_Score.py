score = [234,53,23,35,75,83,8]
highest_score = 0
for n in score:
    if n > highest_score:
        highest_score = n
print(f"The highest score in the class is: {highest_score}")