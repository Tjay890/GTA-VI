import pygame
from location import Location

class Nightclub(Location):
  def __init__(self, name, up, right, down, left, xcoord, ycoord):
    super().__init__(name, up, right, down, left, xcoord, ycoord)

  def enter(self):
    self.inside()

  def inside(self):
    print('You are in the nightclub')
    self.play_sound('nightclub.mp3')
    self.display_image('nightclub.jpeg')
    print('You took too much drugs and died')
    pygame.quit()

  @staticmethod
  def display_image(image_name):
    WINDOW_SIZE = [800, 800]
    screen = pygame.display.set_mode(WINDOW_SIZE)
    Cut = pygame.image.load(image_name).convert()
    screen.blit(Cut, (0, 0))
    pygame.display.flip()
    pygame.time.delay(10000)
    screen.blit(screen, (0, 0))
    pygame.display.flip()

  @staticmethod
  def play_sound(sound_name):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(sound_name)
    pygame.mixer.music.play()