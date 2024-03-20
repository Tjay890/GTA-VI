import pygame, random

#game door Maarten, Jonathan en Tije
pygame.init()
bord = pygame.image.load("LS_Map(met lijntjes).jpg")
WINDOW_SIZE= [800, 800]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("GTA VI(Leak)")
done = False
clock= pygame.time.Clock()

WHITE = (200, 200, 200)
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800



def drawGrid():
      blockSize = 20 #Set the size of the grid block
      for x in range(0, WINDOW_WIDTH, blockSize):
          for y in range(0, WINDOW_HEIGHT, blockSize):
              rect = pygame.Rect(x, y, blockSize, blockSize)
              pygame.draw.rect(screen, WHITE, rect, 1)
while not done:
      screen.fill((255,255,255))
      bordrect = bord.get_rect()
      screen.blit(bord, bordrect)
      clock.tick(60)
      pygame.display.flip()

here = "House"
world = {
  "House" : {
    "transitions": {
      "down" : "Beach",
      "right" : "homie's crip"
    }
  },
  "Beach" : {
    "transitions" : {
      "up" : "House"
    }
  },
  "Homie's crip" : {
    "transitions" : {
      "left" : "House",
      "down" : "Barber",
      "right" : "Freakshop",
      "up" : "Nightclub"
    }
  },
  "Nightclub" : {
    "transitions" : {
      "down" : "Homie's crip",
      "right" : "Casino"
    }
  },
  "Casino" : {
    "transitions" : {
      "left" : "Nightclub",
      "down" : "Freakshop"
    }
  },
  "Freakshop" : {
    "transitions" : {
      "left" : "Homie's crip",
      "up" : "Casino"
    }
  },
  "Barber" : {
    "transitions" : {
      "up" : "Homie's crip",
      "down" : "Docks",
      "left" : "Airport"
    }
  },
  "Docks" : {
    "transitions" : {
      "up" : "Barber"
    }
  },
  "Airport" : {
    "transitions" : {
      "right" : "Barber",
      "left" : "Cayo perigo"
    }
  },
  "cayo perigo" : {
    "transitions" : {
      "right" : "Airport"
    }
  }
}


#vakjes Casino(546, 200), Nightclub(436, 184), Freakshop(501, 279), Barber(439, 450), homies crip(392, 318), Beach(188, 369), Docks(556, 662), house(234, 262), Airport(270, 573), Cayo perigo(114, 454)