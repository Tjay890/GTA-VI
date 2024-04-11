from os import error
import pygame
from location import *
from player import *
from barber import *

class Beach(Location):
  girl = 'no bitches'
  def __init__(self, name, up, right, down, left, xcoord, ycoord):
        super().__init__(name, up, right, down, left, xcoord, ycoord)

  def enter(self):
    print("You are walking to the beach.")
    self.girl = self.hairtype()
  def hairtype(self):
    print("Do want some bitches on your slonggadong ma G?")
    print("You aint looking good with", self.girl, "!")
    a = input(">")
    if a.lower() == "no":
      girl = "no bitches"
      print("Your girl is now", girl, "N***a!")
      return girl
    else:
      print("Wich girl do you want ma g!")
      print("You can chose between these 5 g")
      print("Bald, Blonde, Brunette, Asian or Blacka")
      girl = str(input(">"))
      while (girl.lower() != "bald" and girl != "blonde" and girl != "brunette"
      and girl != "asian" and girl != "blacka"):
        print('Do you like man or som N***a?')
        print('That was not an option')
        print("")
        print("Wich girl do you want ma g!")
        print("You can chose between these 5 g!")
        print("Bald, Blonde, Brunette, Asian or Blacka")
        girl = str(input(">"))
        print("Your girl is now", girl, "N***a!")
        print("")
      if girl == "Bald":
        if player.hair == "Bald":
          self.display_image('Bald.jpg')
          print("You unlocked the crowbar!")
          player.crowbar = 1
          player.inventory.append("crowbar")
        else:
          print("You need yo ass to be bald my guy!")
      elif girl == "Blonde":
        self.display_image('Blonde.jpg')
      elif girl == "Brunette":
        self.display_image('Brunette.jpg')
      elif girl == "Asian":
        self.display_image('Asian.jpg')
        self.play_sound('Indian.mp3')
        self.display_image('Indian.jpg')
        print('It was a man and he f*cked you in the ass')
        print('You died')
        pygame.quit()
      elif girl == "Blacka":
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
  @staticmethod
  def play_sound(sound_name):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(sound_name)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
      pygame.time.Clock().tick(10)