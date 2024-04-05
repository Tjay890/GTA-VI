from location import *
from player import *

#player = Player()
#Boss1 = Stats()


class Cayo(Location):
  def __init__(self, name, up, right, down, left, xcoord, ycoord):
    super().__init__(name, up, right, down, left, xcoord, ycoord)

  def enter(self):
    print("You are going to enter the Bossbattle against El Rubio!")
    self.bossbattle()
    

  def bossbattle(self):
    while player.life >= 0 and Boss1.life >= 0:
      print("chose your Attack")
      print("1:punch")
      print("2:kick")
      print("3:gun")
      print("4:rocketlauncher")
      print("5:heal")
      attack = input(">")
      if attack == "1":
        player.punch()
      elif attack == "2":
        player.kick()
      elif attack == "3":
        player.gun()
      elif attack == "4":
        player.rocketlauncher()
      elif attack == "5":
        player.heal()
      else:
        print("You can not do that.")
    
      print("----------------------")
      Boss1.healthcheck()
      player.healthcheck()
      print("----------------------")
      if player.life >= 0 and Boss1.life >= 0:
        Boss1.attack()
        player.healthcheck()
        print("----------------------")
    
    if Boss1.life > 0:
      print("El Rubio has won with ", Boss1.life, "lifes.")
    else:
      print(" Demarcus has won with ", player.life, "lifes.")
      player.cash += 500
      print(player.cash)