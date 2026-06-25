import random

def dice_roller():
  print("🎲 Welcome to Dice Roller!")
  while True:
    question = input("Roll the dice (y/n): ").lower().strip()
    if question == "y":
      dice = random.randint(1, 6)
      print(f"You rolled: {dice}")
    elif question not in ["y", "n"]:
      print("Please enter y or n")
    elif question == "n":
      print("Thanks for playing!")
      break
    
    
      

dice_roller()