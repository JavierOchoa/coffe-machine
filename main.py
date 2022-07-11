from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeeMaker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

user_is_done = False

while not user_is_done:
    coffee_type = input("What would you like? (espresso/latte/cappuccino/):\n")
    coffee_type.lower()
    if coffee_type not in ["espresso", "latte", "cappuccino"]:
        print("Not a valid option")
    elif coffee_type == "off":
        exit()
    elif coffee_type == "report":
        coffeeMaker.report()
    else:
        item = menu.find_drink(coffee_type)
        print(f"{item.name} is ${item.cost}")
        if coffeeMaker.is_resource_sufficient(item) and money_machine.make_payment(item.cost):
            coffeeMaker.make_coffee(item)
            is_done = input("Is there anything else we could do for you? (y/n)\n")
            if is_done == 'n':
                exit()
