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
    if player.cash <= 0:
      print("It looks like you have got no cash.")
      print("Here is some money")
      player.cash = 100
      print("Your money is now 100")
      input("Press enter")
    elif player.freejoints is False:
      print("Looks like grandma left some joints for you")
      player.joints += 5
      print("You now have",player.joints,"joints.")
      input("Press enter")
      player.freejoints = True
    else:
      print("There is nothing to do here")
      input("Press enter")
      