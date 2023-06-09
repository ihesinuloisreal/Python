MENU = {
    "expresso": {
        "ingredents": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredents": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredents": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }

}

resource = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

# Variable holding reftovers
milk_left = resource["milk"]
water_left = resource["water"]
coffee_left = resource["coffee"]
balance = 0

# Variables holding money value
penny = 0.01
nickel = 0.05
dime = 0.10
quarter = 0.25
switch = True
while switch == True:
    # TODO: Choose Coffee flavor
    choice = input("Choose flavour: Expresso, Latte, or Cappuccino").lower()
    cost = MENU[choice]

    # Input for money to e paid for coffee
    penny *= int(input("Enter your penny "))
    nickel *= int(input("Enter your nickel "))
    dime *= int(input("Enter your dime "))
    quarter *= int(input("Enter your quarter "))
    total = penny + nickel + dime + quarter
    # print(f"Penny = {penny}, Nickel = {nickel}, Dime = {dime}, Quarter = {quarter}")



    # TODO: Print Report
    def report():
        water = resource["water"]
        milk = resource["milk"]
        coffee = resource["coffee"]
        print(f"We have {water}ml of water, {milk}ml of milk and {coffee}ml of coffee left")


    def coffee_processor(choice):
        if choice == "expresso":
            
            output = check_amount(total, cost)
            print(output)
            # print(total - cost["cost"])
        elif choice == "latte":
            # print("Latte")
            output = check_amount(total, cost)
            print(output)
            # cost = MENU["latte"]
            
        elif choice == "cappuccino":
            # print("Cappuccino")
            # cost = MENU["cappuccino"]
            # print(total - cost["cost"])
            output = check_amount(total, cost)
            print(output)
        elif choice == "exit":
            switch = False
        else:
            print("Report")
            report()




    # TODO: Check if amount is enough
    def check_amount(total, cost):
        global balance
        if total == cost["cost"]:
            resource["balance"] += cost["cost"]
            check_ingredent(cost)
            return "You dont have any change"
        elif total < cost["cost"]:
            return "Your money is not enough! Money refund"
        else:
            check_ingredent(cost)
            change = total - cost["cost"]
            balance += cost["cost"]
            return f"You have {change} change left"
            # print("Take change")

            
    # TODO: Chech if ingredents is enough to produce order
    def check_ingredent(cost):
        global water_left
        global coffee_left
        global milk_left
        ingredent = cost["ingredents"]
        if choice == "expresso":
            water_left = water_left - ingredent["water"]
            coffee_left = coffee_left - ingredent["coffee"]
        else:
            milk_left = milk_left - ingredent["milk"]
            water_left = water_left - ingredent["water"]
            coffee_left = coffee_left - ingredent["coffee"]

        
    # TODO: 
    coffee_processor(choice)
    print(f"{milk_left}, {water_left}, {coffee_left}, {balance}")