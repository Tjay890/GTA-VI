from location import *
import random
from player import *

class Casino_games():
  @staticmethod
  def pinapparaat():
    print("This is the secret ATM you can withdraw any amount of money you want")
    print("You have", Stats.cash,"money.")
    extra = int(input("How much money do you want?"))
    Stats.cash += extra
  
  @staticmethod
  def coinflip():
    print("You have", Stats.cash, "money.")
    bet = int(input("How much do you want to bet\n"))
    while bet > Stats.cash:
      print("You dont have that much money.")
      bet = int(input("How much do you want to bet\n"))
    Stats.cash -= bet
    
    print("heads or tails?")
    
    choise = input(">")
    while choise != "heads" and choise != "tails":
      print("Dat kan je niet kiezen")
      choise = input("Kies opnieuw:\n")
    coin = random.randint(0,1)
    if (choise == "heads" and coin == 0) or (choise == "tails" and coin == 1):
      Stats.cash += bet*2
      print("You win your money is doubled.")
      print("You now have",Stats.cash,"money.")
    else:
      print("Your lose")
      
    
  @staticmethod
  def roulette():
    print("roulette shit")
  
  @staticmethod
  def entrance():
    print("Welcome to the ls casino")
    print("you have", Stats.cash, "cash")
    print("You have 1 game you can play.")
    print("""Our current games that are available are:
    1. Heads or Tails.
    2. Roulette.
    """)
    
    choise = input("Choose your game. (press 1 or 2)\n")
    if choise == "1":
      Casino_games.coinflip()
    elif choise == "2":
      Casino_games.roulette()
    elif choise == "69420":
      Casino_games.pinapparaat()
    else:
      print("That is not a game you are going outside")
      
  
  
class Casino(Location):
  def __init__(self, name, up, right, down, left, xcoord, ycoord):
    super().__init__(name, up, right, down, left, xcoord, ycoord)
  def enter(self):
    Casino_games.entrance()