print("Welcome to Python Pizza Deliveries")
size = input("What size of piza do you want? e.g. S, M, L ")

if size == "S":
    bill = 15
    add_pproni = input("Do you want pepperoni? Y or N ")
    if add_pproni == "Y":
        bill += 2
        # print(bill)
    # else:
    #     print(bill)
    extr_cheese = input("Do you want extra cheese? Y or N ")
    if extr_cheese == "Y":
        bill += 1
        print(bill)
    print(bill)

elif size == "M":
    bill = 20
    add_pproni = input("Do you want pepperoni? Y or N ")
    if add_pproni == "Y":
        bill += 3

    extr_cheese = input("Do you want extra cheese? Y or N ")
    if extr_cheese == "Y":
        bill += 1
        print(bill)
    print(bill)
    
elif size == "L":
    bill = 25
    add_pproni = input("Do you want pepperoni? Y or N ")
    if add_pproni == "Y":
        bill += 3
    extr_cheese = input("Do you want extra cheese? Y or N ")
    if extr_cheese == "Y":
        bill += 1
        print(bill)
    print(bill)
    

# print(bill)