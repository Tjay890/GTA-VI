import random
import pygame
from location import *
from player import *
from freakshop import *

class Docks(Location):
  containers = ["Jackpot", "Chinees", "Leeg"]
  
  def __init__(self, name, up, right, down, left, xcoord, ycoord):
    super().__init__(name, up, right, down, left, xcoord, ycoord)


  def enter(self):
    print("You are going to the Docks!(Press enter)")
    input()
    self.check()

  #wanneer je binnekomt
  def check(self):
    if player.crowbar == 1:
      print("You wanna do the heist ma guy?(y/n)")
      antwoord = input(">")
      if antwoord.lower() == "y":
        self.docksheist()
      else:
        self.dockies()
    else:
      self.dockies()
        
      
  
  def docksheist(self):
    print("------------------------------")
    print("Construction Worker: Move yo ass out a here n***a!")
    print("No one: I wouldn't let that slide man!")
    aap = input("Whats yo answere:\n")
    print("Shut up I'll wett you mate.",aap)
    print("------------------------------")
    self.containerplukken()

  
  def containerplukken(self):
    print("Alright, there are 3 containers ahead of you!")
    print("Wich one you chosing, you can only open1.\nAfter that the police will come.")
    print("------------------------------")
    print("You see 3 containers.")
    print("The containers have random shit.\n Choise container 1, 2 or 3.")
    #laad de inhoud van de containers
    self.container = int(input(">"))
    random.shuffle(self.containers)
    if self.containers[(self.container - 1)] =="Jackpot":
      print("Yo ass hit the jackpot, now get the fuck outta here.")
      self.policechase()
    elif self.containers[(self.container - 1)] == "Chinees":
      print("oh oh, you got the Asain girl again, fuck.")
      self.display_image('Asian.jpg')
      self.play_sound('Indian.mp3')
      self.display_image('Indian.jpg')
      print('It was a man and he f*cked you in the ass')
      print('You died')
      pygame.quit()
    else:
      print("Shit, the container is empty, get yo ass in the car.")
      self.policechase()
    # self.rightcontainer = random.randint(1,3)
    # self.chineescontainer = random.randint(1,3)
    # if self.container == self.rightcontainer:
    #   print("Yo ass hit the jackpot, now get the fuck outta here.")
    #   self.policechase()
    # elif self.container == self.chineescontainer:
    #   print("oh oh, you got the Asain girl again, fuck.")
    #   self.display_image('Asian.jpg')
    #   self.play_sound('Indian.mp3')
    #   self.display_image('Indian.jpg')
    #   print('It was a man and he f*cked you in the ass')
    #   print('You died')
    #   pygame.quit()
      
    # else:
    #   print("Shit, the container is empty, get yo ass in the car.")
    #   self.policechase()
  #je getaway driver
  def policechase(self):
    print("The police are comming quick go!")
    if player.driver == "1":
      getaway = random.randint(0, 1)
    elif player.driver == "2":
      getaway = 2
    elif player.driver == "3":
      getaway = 1
    else:
      print("Yo ass ain't got no driver, you gotta run now.")
      getaway = random.randint(-1,1)
      print("You better choose a driver at the freakshop next time.")
    
    if getaway == 1 and self.containers[(self.container - 1)] == "Jackpot":
      print("Yo escaped the police")
      print("Heist is completed")
      print("You earned 2500 cash n***a!")
      player.cash += 2500
      print("Your cash is now:", player.cash)
      print("------------------------------")
    elif getaway == 1 and self.containers[(self.container - 1)] != "Jackpot":
      print("Yo escaped the police")
      print("But you ain't got cash brutha.")
      print("Heist is completed")

    elif getaway == 2:
      print("Mo got away with all the cash, yo ass got robbed N***a.")
    else:
      print("Yo ass got catched by the police man.\n Maybe a better driver next time!")
      pygame.quit()
    
    
    #je prijs
    # if getaway == 1 and self.container == self.rightcontainer:
    #   print("Yo escaped the police")
    #   print("Heist is completed")
    #   print("You earned 2500 cash n***a!")
    #   player.cash += 2500
    #   print("Your cash is now:", player.cash)
    #   print("------------------------------")
    # elif getaway == 1 and self.container != self.rightcontainer:
    #   print("Yo escaped the police")
    #   print("But you ain't got cash brutha.")
    #   print("Heist is completed")
      
    # elif getaway == 2:
    #   print("Mo got away with all the cash, yo ass got robbed N***a.")
    # else:
    #   print("Yo ass got catched by the police man.\n Maybe a better driver next time!")
    #   pygame.quit()
    

  def dockies(self):
    print("Construction Worker: Move yo ass out a here n***a!")
    print("------------------------------")
    input("Press enter.")
  #laad plaatjes en muziek
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