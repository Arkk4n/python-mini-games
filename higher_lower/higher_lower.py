import random
import game_data
import art


def get_random_account():
    return random.choice(game_data.data)


def get_winner(account_a, account_b):
    if account_a["follower_count"] > account_b["follower_count"]:
        return "a"
    else:
        return "b"


def main():
    score = 0
    account_a = get_random_account()
    account_b = get_random_account()
    while True:
        print(
            f"Compare A: {account_a['name']}, {account_a['description']}, {account_a['country']}"
        )
        print(art.vs)
        print(
            f"Compare B: {account_b['name']}, {account_b['description']}, {account_b['country']}"
        )
        guess = input("Who has more followers? Type A or B: ").lower().strip()
        if guess not in ["a", "b"]:
            print("Invalid input")
            continue
        winner = get_winner(account_a, account_b)
        if guess == winner:
            print("You win")
            account_a = account_b
            account_b = get_random_account()
            while account_a == account_b:
                account_b = get_random_account()
            score += 1
            print(f"Current score {score}")
        else:
            print("You lose")
            break
    print(f"Your score is {score}")


main()


# TODO:
# - Add while loop - OK
# - Keep score - OK
# - Move account_b to account_a - OK
# - Generate new account_b - OK

# FIXME:
# Duplicate accounts can appear - DONE
