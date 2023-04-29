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

main_menu = Menu()
# main_menu_item = MenuItem(name, water, milk, coffee, cost)
coffee_m = CoffeeMaker()
money_machine = MoneyMachine()


coffee_m.report()
money_machine.report()
main_menu.get_items()
# main_menu.Name = input("Please Choose your coffee flavor? ")
# money.process_coins()
# money.make_payment(cost)
