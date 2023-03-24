import random
name = input("Type in a word. ")
name_ = name.split()
out = random.randint(0, name_.__len__()-1)

print(f"The number position is {out} and the value is {name_[out]}")