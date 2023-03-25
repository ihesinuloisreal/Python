import random
name = input("Type in the names of persons to play. ")
name_ = name.split()
out = random.randint(0, name_.__len__()-1)

print(f"The number position is {out} and the Person to pay the bills is {name_[out]}")