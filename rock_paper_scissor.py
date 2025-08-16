import random 
import os
options=("rock","paper","scissors")
playing =True

while playing:
  os.system('cls' if os.name == 'nt' else 'clear')
  player=None
  computer=random.choice(options)

  while player not in options:
    player=input("Enter a choice (rock, paper, scissors ): ")
  
  print(f"player: {player}")
  print(f"computer: {computer}")

  if player==computer:
    print("It's a tie! ")

  elif (player=="rock" and computer=="scissors") or (player=="paper" and computer=="rock") or (player=="scissors" and computer=="paper"):
    print("You Win!! ")
  else:
    print("You Lose!!")

  if not input("play again? (y/n): ").lower()=="y":
    playing=False


print("Thanks for playing!!")