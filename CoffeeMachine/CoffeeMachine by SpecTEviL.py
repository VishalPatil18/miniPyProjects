class MenuItem:
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

class Menu:
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=10),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=15),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=20),
        ]

    def get_items(self):
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item
        print("\nSorry that item is not available.")

class MoneyMachine:
    CURRENCY = "Rs"
    COIN_VALUES = {
        "One": 1,
        "Two": 2,
        "Five": 5,
        "Ten": 10
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        print("\nPlease make the payment: ")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many Rs {coin} coins?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"\nHere is {change} {self.CURRENCY} in change.")
            self.profit += cost
            return True
        else:
            print("\nSorry that's not enough money. Money refunded.")
            return False
        self.money_received = 0

class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"\nSorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"\nHere is your {order.name}. Enjoy Your COFFEE!")

running = True
menu = Menu()
name = menu.get_items()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
print("========= Welcome to SpecTEviL's Coffee Shop =========")
print("=============== The Menu is as follows ===============")
print("* Latte -> 10 Rs")
print("* Espresso -> 15 Rs")
print("* Cappuccino -> 20 Rs")
while running:
    choice = input(f"\nWhat would you like to order?\n\t1) espresso\t2) latte\n\t3) cappuccino   4) nothing:\n")
    if choice == "nothing":
        running= False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

