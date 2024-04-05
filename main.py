import wereld
import pygame

from pygame.constants import KEYDOWN

#game door Maarten, Jonathan en Tije
pygame.init()
#startvariablen
bord = pygame.image.load("LS_Map(met lijntjes).jpg")
WINDOW_SIZE= [800, 800]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("GTA VI(Leak)")
done = False
clock= pygame.time.Clock()
hair = "Default"
current = "House"
while not done:
      screen.fill((255,255,255))
      bordrect = bord.get_rect()
      screen.blit(bord, bordrect)
      clock.tick(60)
      pygame.display.flip()
      current = wereld.move(current)
      








