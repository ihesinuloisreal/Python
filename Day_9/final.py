from os import system

auction = {}
reply = True
while reply == True:
    name = input("Whats your name: ")
    amount = input("How much would you want to bid: $")
    auction[name] = amount
    response = input("Is there any other Bider")
    if response == "no" :
        reply = False
    system('cls')
    

highest = 0

for key in auction:
    value = int(auction[key])
    if value > highest:
        highest=value
    else:
        highest = highest
print(highest)
print(auction)