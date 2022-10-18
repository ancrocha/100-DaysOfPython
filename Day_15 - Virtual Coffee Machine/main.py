from multiprocessing.spawn import prepare


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
    "money": 0,
}


def check_resources(choice):
    for item in MENU[choice]['ingredients']:
        if resources[item] < MENU[choice]['ingredients'][item]:
            print(f"Sorry there is not enough {item}")


def collect_coins(choice):
    global resources
    print("Please insert coins.")
    quarters = float(input("How many quarters?: ") or 0) * 0.25
    dimes = float(input("How many dimes?: ") or 0) * 0.1
    nickles = float(input("How many nickles?: ") or 0) * 0.05
    pennies = float(input("How many pennies?: ") or 0) * 0.01

    drink_price = float(MENU[choice]['cost'])
    total_money = quarters + dimes + nickles + pennies

    if total_money >= drink_price:
        change = total_money - drink_price
        print(f"Here is ${change} in change.")
        resources.update({'money': drink_price})
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def prepare_drink(choice):
    print(choice)


is_on = True


while is_on == True:
    user_selection = input("What would you like? (espresso/latte/cappuccino):")

    if user_selection == "off":
        is_on = False
    elif user_selection == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
    else:
        if user_selection in MENU:
            check_resources(user_selection)
            paid = collect_coins(user_selection)
            if paid:
                prepare_drink(user_selection)
            else:
                prepare_drink("not proceed")
        else:
            print("your choice does not exist")
