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
    elif user_selection == "espresso":
        check_resources("espresso")
    elif user_selection == "latte":
        check_resources("latte")
    elif user_selection == "cappuccino":
        check_resources("cappuccino") 
    else:
        print("your choice does not exist")     



