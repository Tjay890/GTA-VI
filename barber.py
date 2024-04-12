from location import *
import pygame
from player import *

class Barber(Location):
  player.hair = "YEYEASSHAIRCUT"
  haircuts = ["buzz","fringe", "mullet", "bald", "default"]
  def __init__(self, name, up, right, down, left, xcoord, ycoord):
    super().__init__(name, up, right, down, left, xcoord, ycoord)
    
  def enter(self):
    print("You are going inside.(Press enter)")
    input()
    player.hair = self.hairstyle()
  #als je de barber binnekomt
  def hairstyle(self):
    print("Do want a haircut ma G?\nYou aint looking fresh with that",player.hair,"!")
    a = input(">")
    #als je nee zegt
    if a.lower() == "no":
      hair = "YEYEASSHAIRCUT"
      print("Yo hairstyle is now", hair, "N***a!")
      return hair
    #als je iets anders typed
    else:
      print("Wich haircut do you want ma n***a!")
      print("You can chose between these 5 n***a!")
      print("Buzz, Fringe, Mullet, Bald or Default")
      hair = str(input(">"))
      #zorgt dat je wel een echt kapsel in vult
      while (hair not in self.haircuts):
        print("You cannot chose that n***a !\nChoose again!")
        print("")
        print("Wich haircut do you want ma n***a!")
        print("You can chose between these 5 n***a!")
        print("Buzz, Fringe, Mullet, Bold or Default")
        hair = str(input(">"))
      print("Yo hairstyle is now", hair, "N***a!")
      print("")
      #kijkt welk haar je kiest
      if hair.lower() == "buzz":
        self.display_image('Buzz.jpg')
      if hair.lower() == "fringe":
        self.display_image('Fringe.jpg')
      if hair.lower() == "mullet":
        self.display_image('Mullet.jpg')
      if hair.lower() == "bald":
        self.display_image('Bold.jpg')
      if hair.lower() == "default":
        self.display_image('Default.jpg')
      return hair
  #laadt de fotos
  @staticmethod
  def display_image(image_name):
    WINDOW_SIZE = [800, 800]
    screen = pygame.display.set_mode(WINDOW_SIZE)
    Cut = pygame.image.load(image_name).convert()
    screen.blit(Cut, (0, 0))
    pygame.display.flip()
    pygame.time.delay(2000)
    screen.blit(screen, (0, 0))
    pygame.display.flip()