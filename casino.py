from location import *
import random
from player import *

class Casino_games():
  @staticmethod
  def coinflip():
    print("You have", Stats.cash, "money.")
    play = input("Do you want to play?(y/n)")
    if play == "n":
      exit()
    print("heads or tails?")
    
    choise = input(">")
    coin = random.randint(0,1)
    if (choise.lower == "heads" and coin == 0) or (choise.lower == "tails" and coin == 1):
      print("You win your money is doubled.")
    else:
      
      print("Your lose")
      
    
  @staticmethod
  def roulette():
    print("roulette shit")
  
  @staticmethod
  def entrance():
    print("Welcome to the ls casino")
    print("You have 1 game you can play.")
    print("""Our current games that are available are:
    1. Heads or Tails.
    2. Roulette.
    """)
    print("you have", Stats.cash, "cash")
    choise = input("Choose your game. (press 1 or 2)")
    if choise == "1":
      Casino_games.coinflip()
    elif choise == "2":
      Casino_games.roulette()
    else:
      pass
  
  
class Casino(Location):
  def __init__(self, name, up, right, down, left, xcoord, ycoord):
    super().__init__(name, up, right, down, left, xcoord, ycoord)
  def enter(self):
    Casino_games.entrance()