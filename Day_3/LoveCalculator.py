Your_Name = input("What is your name? ")
Your_crush_name = input("What is your crush/admirer name? ")
a = 0
b = 0

a += Your_Name.lower().count("t")
a += Your_Name.lower().count("r")
a += Your_Name.lower().count("u")
a += Your_Name.lower().count("e")

a += Your_crush_name.lower().count("t")
a += Your_crush_name.lower().count("r")
a += Your_crush_name.lower().count("u")
a += Your_crush_name.lower().count("e")

b += Your_Name.lower().count("l")
b += Your_Name.lower().count("o")
b += Your_Name.lower().count("v")
b += Your_Name.lower().count("e")

b += Your_crush_name.lower().count("l")
b += Your_crush_name.lower().count("o")
b += Your_crush_name.lower().count("v")
b += Your_crush_name.lower().count("e")
print(f"{a}{b}")