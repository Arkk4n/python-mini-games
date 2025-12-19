print("You are in stone room and you see the doors directed on north, chest and torch.\n")

has_key = False
chest_opened = False
torch_lit = False
running = True
moves = 0
look = ""
while running:
    player_choice = input("Write your decision, what to do:\n")
    moves += 1
    if player_choice == "help":
        print("Commands: look, open chest, take key, light torch, north, q")
    elif player_choice == "look":
        print("\nYou look around:")
        print("- There is a door to the north.")
        print(f"- The chest is {'open' if chest_opened else 'closed'}.")
        if chest_opened and not has_key:
            print("- You see an old key in the chest.")
        elif chest_opened and has_key:
            print("- The chest is empty.")
        print(f"- The torch is {'lit' if torch_lit else 'unlit'}.\n")

    elif player_choice == "open chest":
        if chest_opened:
            print("It's already open.")
        else:
            chest_opened = True
            print("You open the chest.")

    elif player_choice == "take key":
        if not chest_opened:
            print("No key here.")
        elif has_key:
            print("You already have it.")
        else:
            has_key = True
            print("You take the key.")

    elif player_choice == "north":
        if has_key:
            print(f"You unlock the door and escape. You win! (moves: {moves})")
            break
        else:
            print("The door is locked.")

    elif player_choice == "q":
        print(f"Goodbye! moves: {moves}")
        break
    else:
        print("Invalid command.")

