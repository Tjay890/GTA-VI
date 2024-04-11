#importeert de zooi die je nodig hebt
import wereld
import pygame
from pygame import mixer
from pygame.constants import KEYDOWN

#game door Maarten, Jonathan en Tije
#Start pygame en het geluid op
pygame.init()
mixer.init()
mixer.music.load('Music.mp3')
mixer.music.play(-1)

#startvariablen
bord = pygame.image.load("Bord.jpg")
bordrect = bord.get_rect()
#maakt het scherm
WINDOW_SIZE= [800, 800]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("GTA VI(Leak)")
done = False
clock= pygame.time.Clock()

current = "House"

WHITE = (200, 200, 200)
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800
#laad het hoofd in
player_image = pygame.image.load("Head.jpg")
player_rect = player_image.get_rect()

while not done:
  player_x = wereld.world[current].x
  player_y = wereld.world[current].y
  screen.fill((255,255,255))
  player_rect.center = bordrect.center
  screen.blit(bord, bordrect)
  player_rect.center = (player_x, player_y)
  screen.blit(player_image, player_rect)
  clock.tick(60)
  pygame.display.flip()
  current = wereld.move(current)









#vakjes Casino(546, 200), Nightclub(436, 184), Freakshop(501, 279), Barber(439, 450), homies crip(392, 318), Beach(188, 369), Docks(556, 662), house(234, 262), Airport(270, 573), Cayo perigo(114, 454)




