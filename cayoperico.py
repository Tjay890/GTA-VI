from location import *
from player import *

#player = Player()
#Boss1 = Stats()


class Cayo(Location):
  def __init__(self, name, up, right, down, left, xcoord, ycoord):
    super().__init__(name, up, right, down, left, xcoord, ycoord)
  #wanneer je de cayo binnen komt
  def enter(self):
    print("You are going to enter the Bossbattle against El Rubio!(Press enter)")
    input()
    self.storyline()
  #story
  def storyline(self):
    print("El Rubio: ZzZzZzZzZz, ZzZzzZ")
    print("El Rubio: uhhh, who da f* are you man.")
    naam = input(">")
    print("El Rubio: Uhmmm, I know yo ass," + naam)
    print(naam + ":You sure you know me?")
    print(naam+":I whoope yo ass man")
    print("El Rubio: We will see!")
    print("===========================")
    self.bossbattle()

  #jouw attacks
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
      #laat de status van jouw levens en die van de boss zien
      print("----------------------")
      Boss1.healthcheck()
      player.healthcheck()
      print("----------------------")
      if player.life >= 0 and Boss1.life >= 0:
        Boss1.attack()
        player.healthcheck()
        print("----------------------")
    #als 1 van de 2 dood is
    if Boss1.life > 0:
      print("El Rubio has won with ", Boss1.life, "lifes.")
    else:
      print(" Demarcus has won with ", player.life, "lifes.")
      player.cash += 5000
      print("Yo ass won 5000 dollaarsss!!!! n***a!!")
      print("Your cash is now:", player.cash)
      
