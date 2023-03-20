Your_Name = input("What is your name? ")
Your_crush_name = input("What is your crush/admirer name? ")

possible = Your_crush_name + Your_Name
a = 0
b = 0

a += possible.lower().count("t")
a += possible.lower().count("r")
a += possible.lower().count("u")
a += possible.lower().count("e")

b += possible.lower().count("l")
b += possible.lower().count("o")
b += possible.lower().count("v")
b += possible.lower().count("e")

outcome = int(f"{a}{b}") 

if outcome < 10 or outcome > 90:
    print(f"Your score is {outcome}, You guys are compatible")
elif outcome >= 40 and outcome <= 50:
    print(f"Your score is {outcome}, You guys are alright together")
else:
    print(f"Your score is {outcome}")
    