import random
import game_data


def get_random_account():
    account = random.choice(game_data.data)
    return account


account = get_random_account()
print(account["name"])
print(account["description"])
print(account["country"])
