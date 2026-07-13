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
    },
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


machine_is_on = True

while machine_is_on:
    client_input = (
        input("What would you like? (espresso/latte/cappuccino)").strip().lower()
    )
    if client_input == "off":
        print("Turn off")
        machine_is_on = False
    elif client_input == "report":
        print(resources)
    elif client_input in MENU:
        drink = MENU[client_input]
        print(drink)
    else:
        print("Unknown option.")
