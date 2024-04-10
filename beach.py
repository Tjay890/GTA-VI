from location import *
import pygame

class Beach(Location):
  girl = 'no bitches'
  def __init__(self, name, up, right, down, left, xcoord, ycoord):
    super().__init__(name, up, right, down, left, xcoord, ycoord)
    
  def enter(self):
    print("You are walking to the beach.")
    self.girl = self.hairtype()

  def hairtype(self):
    print("Do want a some bitches on your slonggadong ma G?")
    print("You aint looking good with ",self.girl,"!")
    a = input(">")
    if a.lower() == "no":
      girl = "no bitches"
      print("Yo girl is now", girl, "N***a!")
      return girl
    else:
      print("Wich girl do you want ma g!")
      print("You can chose between these 5 g")
      print("Bald, Blonde, Brunette, Asian or Blacka")
      girl = str(input(">"))
      while (girl != "Bald" and girl != "Blond" and girl != "Brunette"
      and girl != "Asian" and girl != "Blacka"):
        print('Do you like man or som N***a?')
        print('That was not an option')
        print("")
        print("Wich haircut do you want ma g!")
        print("You can chose between these 5 g!")
        print("Bald, Blonde, Brunette, Asian or Blacka")
        girl = str(input(">"))
        print("Yo girl is now", girl, "N***a!")
        print("")
      if girl == "Bald":
        self.display_image('Bald.jpg')
      if girl == "Blonde":
        self.display_image('Blonde.jpg')
      if girl == "Brunette":
        self.display_image('Brunette.jpg')
      if girl == "Asian":
       self.display_image('Asian.jpg')
      if girl == "Blacka":
       self.display_image('Blacka.jpg')
      return girl
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