MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

currency = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01
}

is_on = True  # decides if coffee machine is on
money_in_machine = 0.00  # total money in the coffee machine (per customer)


# TODO: 3. Print report
def print_report():
    for ingredient in resources:  # 'ingredient' is a key, and the amt is the value
        print(ingredient, ": ", resources[ingredient], "ml")
    # TODO: 3a. Print money amount entered


while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "espresso":
        print("e")
    elif choice == "latte":
        print("l")
    elif choice == "cappuccino":
        print("c")
    elif choice == "report":
        print_report()
    elif choice == "off":
        print("Thanks for using the coffee machine! See you later")
        is_on = False
    else:
        print("Not a valid choice")
