from location import *
from player import *




class Airport(Location):
  def __init__(self, name, up, right, down, left, xcoord, ycoord):
    super().__init__(name, up, right, down, left, xcoord, ycoord)
  def ticketbooth(self):
    print("Welcome to the ticket booth.")
    print("Here you can buy a ticket to Cayo Perico.")
    print("A ticket is 1000 cash.")
    shop = input("Would you like to buy a ticket?(y/n)\n")
    print()
    if shop== "y" and player.cash >= 1000:
      player.cash -= 1000
      ticket = True
      print("You have bought a ticket to Cayo Perico.")
      print("Have a nice flight!")
      print()
    elif player.cash < 1000:
      print("You dont have enough money.")
      print("Come back once you have filled yo pockets.")
      ticket = False
    else:
      print("Aight, come back when you have changed yo mind")
      ticket = False
    return ticket
  def enter(self):
    print("You are going inside.")
    print()
    player.ticket = self.ticketbooth()
