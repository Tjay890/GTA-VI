import random
from location import *
from player import *
from freakshop import *

class Docks(Location):
  def __init__(self, name, up, right, down, left, xcoord, ycoord):
    super().__init__(name, up, right, down, left, xcoord, ycoord)


  def enter(self):
    print("Press enter to enter the Docks!")
    input()
    self.check()


  def check(self):
    if player.crowbar == 1:
      print("You wanna do the heist ma guy?")
      antwoord = input(">")
      if antwoord.lower() == "yes":
        self.docksheist()
      else:
        self.dockies()
    else:
      self.dockies()
        
      

  def docksheist(self):
    print("------------------------------")
    print("Construction Worker: Move yo ass out a here n***a!")
    print("No one: I wouldn't let that slide man!")
    aap = input("Whats yo answere:")
    print("Shut up I'll wett you mate.",aap)
    print("------------------------------")
    self.containerplukken()

  
  def containerplukken(self):
    print("Alright, there are 3 containers ahead of you!")
    print("Wich one you chosing, you can only open1.\nAfter that the police will come.")
    print("------------------------------")
    print("You see 3 containers.")
    print("The containers have random shit.\n Choise container 1, 2 or 3.")
    self.container = int(input(">"))
    self.rightcontainer = random.randint(1,3)
    self.chineescontainer = random.randint(1,3)
    if self.container == self.rightcontainer:
      print("Yo ass hit the jackpot, now get the fuck outta here.")
      self.policechase()
    elif self.container == self.chineescontainer:
      print("oh oh, you got the Asain girl again, fuck.")
    else:
      print("Shit, the container is empty, get yo ass in the car.")
      self.policechase()

  def policechase(self):
    print("The police are comming quick go!")
    if player.driver == "1":
      getaway = random.randint(0, 2)
    elif player.driver == "2":
      getaway = 2
    elif player.driver == "3":
      getaway = 1
    else:
      print("Yo ass ain't got no driver, you gotta run now.")
      getaway = 3
      print("You better choose a driver at the freakshop next time.")
    if getaway == 1 and self.container == self.rightcontainer:
      print("Yo escaped the police")
      print("Heist is completed")
      print("You earned 2500 cash n***a!")
      player.cash += 2500
      print("Your cash is now:", player.cash)
      print("------------------------------")
    elif getaway == 1 and self.container != self.rightcontainer:
      print("Yo escaped the police")
      print("But you ain't got cash brutha.")
      print("Heist is completed")
      
    elif getaway == 2:
      print("Mo got away with all the cash, yo ass got robbed N***a.")
    else:
      print("Yo ass got catched by the police man.\n Maybe a better driver next time!")
    

  def dockies(self):
    print("Construction Worker: Move yo ass out a here n***a!")
    print("------------------------------")
    input("Press enter.")