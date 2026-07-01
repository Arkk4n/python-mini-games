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
    account_a = get_random_account()
    account_b = get_random_account()
    print(
        f"Compare A: {account_a['name']}, {account_a['description']}, {account_a['country']}"
    )
    print(art.vs)
    print(
        f"Compare B: {account_b['name']}, {account_b['description']}, {account_b['country']}"
    )
    guess = input("Who has more followers? Type A or B: ").lower().strip()
    if guess not in ["a", "b"]:
        return "Invalid input"
    winner = get_winner(account_a, account_b)
    if guess == winner:
        print("You win")
    else:
        print("You lose")


main()
