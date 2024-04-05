from location import *
import random
import math
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
  #roulette spel met dank aan https://stackoverflow.com/questions/52828074/roulette-program-adding-up-the-cash en nog een beetje aangepast zodat het werkt met onze code
  def roulette():
    exit = False
    while exit is False:  
        print('Place your bet! ',Stats.cash,'bucks!', '''
    =======================================
    1. Bet on Red (pays 1:1)
    2. Bet on Black (pays 1:1)
    3. First 12 (pays 2:1)
    4. Middle 12 (pays 2:1)
    5. Last 12 (pays 2:1)
    6. Choose any number (pays 35:1)
    7. Cash out
    Please enter your choice: ''')
        menuChoice = int(input())
        #Add validation!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        if Stats.cash > 0 and menuChoice != 7: #Determine if quit or broke
            if menuChoice == 6:
                number = int(input('Please choose a number from 0-36!')) #Get their specific number
                while number < 0 or number > 36: #Validation
                    number = int(input('Please enter a number from 0-36'))


            wager = int(input('How much would you like to bet? '))
            #Add validation!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            while wager > Stats.cash:
              print("You dont have that much money.")
              wager = int(input("How much would you like to bet?"))
              
              
              
            print('Press any key to spin the wheel! ')
            input()
            print(menuChoice, wager)
    ##
            ball = random.randint(0,36)


            if ball == 0:
                color = ('green')
            elif ball % 2 == 0:
                color = ('black')
            else:
                color = ('red')

            print('Your ball was',ball, 'and landed on the color',color)

            #Determine if winner
            if menuChoice == 1 and color == 'red':
                winner = True
                odds = 1

            elif menuChoice == 2 and color == 'black':
                winner = True
                odds = 1

            elif menuChoice == 3 and ball >= 1 and ball <= 12 :
                winner = True
                odds = 2

            elif menuChoice == 4 and ball >= 13 and ball  <= 24:
                winner = True
                odds = 2

            elif menuChoice == 5 and ball >= 25 and ball  <= 36:
                winner = True
                odds = 2

            elif menuChoice == 6 and ball == number:
                winner = True
                odds = 35

            else:
                winner = False
                odds = 0

                #End determine if winner

            if odds == 0:
                pass
            else:
                amount = wager * odds   #Get amount won/lost
                print(amount)

            if winner == True:
                Stats.cash += amount #<~~~~~~~~~~~~~Problem Area
                print('Congratulations! You won', wager,'dollars!')
                print('Your total is now :',Stats.cash,'dollars.')
            else:
                Stats.cash -= wager
                print('Sorry! You lost',wager,'dollars. Better luck next time!')
                print('Your total is now :',Stats.cash,'dollars.')

            input('Press a key to go back to the menu!')

            print('====================================================================')

            #New round





        else:
            print('Thank you for playing! ')
            exit = True
  
  @staticmethod
  #binnenkomst bij casino
  def entrance():
    #zorgen dat je in het casino blijft
    exit = False
    print("Welcome to the ls casino")
    
    while exit is False:
      
      print("you have", Stats.cash, "cash")
      print("You have 1 game you can play.")
      print("""Our current games that are available are:
      1. Heads or Tails.
      2. Roulette.
      3. Exit.
      """)
      
      choise = input("Choose your game. (press 1 or 2)\n")
      #check welke minigame je gaat doen
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