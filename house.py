from location import *
from player import *
class House(Location):
  def __init__(self, name, up, right, down, left, xcoord, ycoord):
    super().__init__(name, up, right, down, left, xcoord, ycoord)
  def enter(self):
    self.inside()
  @staticmethod
  def inside():
    print("You are currently in you own house.")
    if Stats.cash <= 0:
      print("It looks like you have got no cash.")
      print("Here is some money")
      Stats.cash = 100
      print("Your money is now 100")
      input("Press enter")
    else:
      print("Looks like grandma left some cookies for you")
      Stats.cookies1 += 5
      print("You now have",Stats.cookies1,"cookies.")
      input("Press enter")
      