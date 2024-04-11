from location import *
from player import *

class Freakshop(Location):
  def __init__(self, name, up, right, down, left, xcoord, ycoord):
    super().__init__(name, up, right, down, left, xcoord, ycoord)

  

  
  def enter(self):
    print("Press enter to enter the freakshop!")
    self.story()
  
  
  def story(self):
    if player.crowbar == 1:
      print("Pablo: So you got the crowbar.\n Go to the docks and open a container.")
      print("Pablo: Yo driver will wait there with the getaway car.")
      print("---------------------------------")
    else:
      print("Pablo: Uhmmmm, you ready?")
      input("DeMarcus:")
      print("Pablo: You have no choice man!")
      print("Pablo: Let's begin!")
      print("---------------------------------")
      self.chosing()

  def chosing(self):
    print("Pablo: First you have to chose yo crew man")
    print("Pablo: Chose wisely, yo ass may get scammed!!")
    print("---------------------------------")
    print ("Chose the driver:\n 1:Rashid\n 2:Mo\n 3:Jayquavion")
    player.driver = input(">")
    print("Ai, wise choise amigo!")
    print("---------------------------------")
    self.startheist()


#starting the heist
  def startheist(self):
    print("First you need a crowbar.\n You can find one at the beach.")
    print("Once you have the crowbar, comeback.")



   
    
    