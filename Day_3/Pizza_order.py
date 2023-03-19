print("Welcome to Python Pizza Deliveries")
size = input("What size of piza do you want? e.g. S, M, L ")
extr_cheese = input("Do you want extra cheese? Y or N ")

if size == "S":
    bill = 15
    add_pproni = input("Do you want pepperoni? Y or N ")
    if add_pproni == "Y":
        bill += 2
        print(bill)
    else:
        print(bill)

elif size == "M":
    bill = 20
    if add_pproni == "Y":
        bill += 3
    
elif size == "L":
    bill = 25
    if add_pproni == "Y":
        bill += 3
else:
    print(bill)
    

print(bill)