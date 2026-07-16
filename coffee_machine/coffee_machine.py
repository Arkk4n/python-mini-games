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
            user_quarters = int(input("How many quarters?: "))
            quarters = user_quarters * 0.25
            user_dimes = int(input("How many dimes?: "))
            dimes = user_dimes * 0.10
            user_nickles = int(input("How many nickles?: "))
            nickles = user_nickles * 0.05
            user_pennies = int(input("How many pennies? "))
            pennies = user_pennies * 0.01

            entered_coins = quarters + dimes + nickles + pennies
            print(entered_coins)

            if entered_coins == drink["cost"]:
                print("Your drink is prepared.")
            elif entered_coins < drink["cost"]:
                print("Not enough money for drink, please enter more coins.")
            else:
                print("You inserted more money, here is your back.")
    else:
        print("Unknown option.")
