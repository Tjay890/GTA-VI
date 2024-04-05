from location import *
import random
from player import *

class Casino_games():
  @staticmethod
  #geheim pinapparaat waar je je cash kan opladen
  def pinapparaat():
    print("This is the secret ATM you can withdraw any amount of money you want")
    print("You have", Stats.cash,"money.")
    extra = int(input("How much money do you want?"))
    Stats.cash += extra
  
  @staticmethod
  #Kop of munt minigame
  def coinflip():
    print("You have", Stats.cash, "money.")
    #inzet
    bet = input("How much do you want to bet. (Type a number or all in)\n")
    #kijken of je all in doet en anders je inzet in een nummer veranderen
    if bet == "all in":
      bet = Stats.cash
    else:
      bet = int(bet)
      #checken of je inzet niet meer is dan je hebt
      while bet > Stats.cash:
        print("You dont have that much money.")
        bet = input("How much do you want to bet. (Type a number or all in)\n")
    
    #geld dat je ingezet hebt van je totale geld afhalen
    Stats.cash -= bet
    
    print("heads or tails?")
    
    choise = input(">")
    #zorgen dat je een goede keus maakt
    while choise != "heads" and choise != "tails":
      print("Dat kan je niet kiezen")
      choise = input("Kies opnieuw:\n")
    coin = random.randint(0,1)
    #checken of jouw keuze gelijk is aan wat de uitkomst was
    if (choise == "heads" and coin == 0) or (choise == "tails" and coin == 1):
      Stats.cash += bet*2
      print("You win your money is doubled.")
      print("You now have",Stats.cash,"money.")
    else:
      print("Your lose")
      
    
  @staticmethod
  #roulette spel
  def roulette():
    print("roulette shit")
  
  @staticmethod
  #binnenkomst bij casino
  def entrance():
    exit = False
    print("Welcome to the ls casino")
    
    while exit is False:
      
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
      elif choise == "3":
        exit = True
        print("You are going outside.")
      elif choise == "69420":
        Casino_games.pinapparaat()
      else:
        print("That is not a game")
      
  
  
class Casino(Location):
  def __init__(self, name, up, right, down, left, xcoord, ycoord):
    super().__init__(name, up, right, down, left, xcoord, ycoord)
  def enter(self):
    Casino_games.entrance()