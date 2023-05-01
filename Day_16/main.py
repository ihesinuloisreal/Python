# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.color("cyan")
# timmy.shape("turtle")
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# from prettytable import PrettyTable
# table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = "l"
# print(table)

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
# menu_item = MenuItem(name, water, milk, coffee, cost)
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


# coffee_maker.report()
# money_machine.report()
choice = input(f"Choose flavour: {menu.get_items()}")

if choice == "report":
    coffee_maker.report()
    money_machine.report()

else:
    choice_out = menu.find_drink(choice)
    out = coffee_maker.is_resource_sufficient(choice_out)
    if out == True:
        money_machine.make_payment(choice_out.cost)
        coffee_maker.make_coffee(choice_out)
        money_machine.report()


        # print(result)



