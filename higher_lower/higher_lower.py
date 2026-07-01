import random
import game_data
import art


def get_random_account():
    return random.choice(game_data.data)


account_a = get_random_account()
account_b = get_random_account()

print(
    f"Compare A: {account_a['name']}, {account_a['description']}, {account_a['country']}"
)
print(art.vs)
print(
    f"Compare B: {account_b['name']}, {account_b['description']}, {account_b['country']}"
)
