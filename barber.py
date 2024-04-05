from location import *
import pygame
from player import *
class Barber(Location):
  hair = "YEYEASSHAIRCUT"
  def __init__(self, name, up, right, down, left, xcoord, ycoord):
    super().__init__(name, up, right, down, left, xcoord, ycoord)
    
  def enter(self):
    print("You are going inside.")
    self.hair = self.hairstyle()

  def hairstyle(self):
    print("Do want a haircut ma G?\nYou aint looking fresh with that",self.hair,"!")
    a = input(">")
    if a.lower() == "no":
      hair = "YEYEASSHAIRCUT"
      print("Yo hairstyle is now", hair, "N***a!")
      return hair
    else:
      print("Wich haircut do you want ma n***a!")
      print("You can chose between these 5 n***a!")
      print("Buzz, Fringe, Mullet, Bold or Default")
      hair = str(input(">"))
      while (hair != "Buzz" and hair != "Fringe" and hair != "Mullet"
             and hair != "Bold" and hair != "Default"):
        print("You cannot chose that n***a !\nChoose again!")
        print("")
        print("Wich haircut do you want ma n***a!")
        print("You can chose between these 5 n***a!")
        print("Buzz, Fringe, Mullet, Bold or Default")
        hair = str(input(">"))
      print("Yo hairstyle is now", hair, "N***a!")
      print("")
      if hair == "Buzz":
        self.display_image('Buzz.jpg')
      if hair == "Fringe":
        self.display_image('Fringe.jpg')
      if hair == "Mullet":
        self.display_image('Mullet.jpg')
      if hair == "Bold":
        self.display_image('Bold.jpg')
      if hair == "Default":
        self.display_image('Default.jpg')
      return hair
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
