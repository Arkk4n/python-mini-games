import random

def coin_flip():
  print("🪙 Coin Flip Game")
  options = ["Heads", "Tails"]
  heads = 0
  tails = 0
  while True:
    player = input("Flip the coin? (y/n): ").lower().strip()
    if player == "y":
      computer = random.choice(options)
      print(f"You got {computer}")
      if computer == "Heads":
        heads += 1
        print(f"Heads: {heads}")
      else:
        tails += 1
        print(f"Tails: {tails}")
    elif player == "n":
      print("Thanks for playing")
      break
    else:
      print("Please enter y or n")
    
    
coin_flip()
  