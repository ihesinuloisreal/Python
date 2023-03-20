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
print(f"{a}{b}")