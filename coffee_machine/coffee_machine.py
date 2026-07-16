import menu

machine_is_on = True

while machine_is_on:
    client_input = (
        input("What would you like? (espresso/latte/cappuccino)").strip().lower()
    )
    if client_input == "off":
        print("Turn off")
        machine_is_on = False
    elif client_input == "report":
        print(menu.resources)
    elif client_input in menu.MENU:
        drink = menu.MENU[client_input]
        print(drink["cost"])
        print(drink["ingredients"])
        are_resources_enough = True
        for ingredient, needed_amount in drink["ingredients"].items():
            if needed_amount > menu.resources[ingredient]:
                print(f"Not enough {ingredient}")
                are_resources_enough = False
        if are_resources_enough:
            pass
    else:
        print("Unknown option.")
