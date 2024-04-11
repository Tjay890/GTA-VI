from location import *

class Freakshop(Location):
  def __init__(self, name, up, right, down, left, xcoord, ycoord):
    super().__init__(name, up, right, down, left, xcoord, ycoord)

  driver = 0
  guns = 0
  cut = 0

  
  def enter(self):
    print("Press enter to enter the freakshop!")
    self.starthesit()
  
  
  def story(self):
    print("Pablo: Uhmmmm, you ready?")
    input("DeMarcus:")
    print("Pablo: You have no choice man!")
    print("Pablo: Let's begin!")
    print("---------------------------------")
    

  def chosing(self):
    print("Pablo: First you have to chose yo crew man")
    print("Pablo: Chose wisely, yo ass may get scammed!!")
    print("---------------------------------")
    print ("Chose the driver:\n 1:Rashid\n 2:Mo\n 3:Jayquavion")


  def starthesit(self):
    self.story()
    