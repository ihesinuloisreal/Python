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
penny = 0.01
nickel = 0.05
dime = 0.10
quarter = 0.25

penny *= int(input("Enter your penny "))
nickel *= int(input("Enter your nickel "))
dime *= int(input("Enter your dime "))
quarter *= int(input("Enter your quarter "))
total = penny + nickel + dime + quarter
print(f"Penny = {penny}, Nickel = {nickel}, Dime = {dime}, Quarter = {quarter}")



# TODO: Print Report
def check_ingredent():
    water = resource["water"]
    milk = resource["milk"]
    coffee = resource["coffee"]
    print(f"We have {water}ml of water, {milk}ml of milk and {coffee}ml of coffee left")

# TODO: Choose Coffee flavor
choice = input("Choose flavour: ").lower()
if choice == "expresso":
    # print("expresso")
    cost = MENU["expresso"]
    print(total - cost["cost"])
elif choice == "latte":
    # print("Latte")
    cost = MENU["latte"]
    change = total - cost["cost"]
    print(f"You have {change} change left")
elif choice == "cappuccino":
    print("Cappuccino")
    cost = MENU["cappuccino"]
    print(total - cost["cost"])
else:
    print("Report")
    check_ingredent()
# TODO: Check if amount is enough
# TODO: Chech if ingredents is enough to produce order
# TODO: 