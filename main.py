import pygame, random

#game door Maarten, Jonathan en Tije
pygame.init()

bord = pygame.image.load("LS_Map(met lijntjes).jpg")
bordrect = bord.get_rect()

WINDOW_SIZE= [800, 800]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("GTA VI(Leak)")
done = False
clock= pygame.time.Clock()

WHITE = (200, 200, 200)
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800

#location =  [[546, 200], [436, 184], [501, 279], [439, 450], [392, 318], [188, 369], [556, 662], [234, 262], [270, 573], [114, 454]]

player_image = pygame.image.load("Head.jpg")
player_rect = player_image.get_rect()

while not done:
      screen.fill((255,255,255))
      player_rect.center = bordrect.center
      screen.blit(bord, bordrect)
      screen.blit(player_image, player_rect)
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


#vakjes Casino(546, 200), Nightclub(436, 184), Freakshop(501, 279), Barber(439, 450), homies crip(392, 318), Beach(188, 369), Docks(556, 662), house(234, 262), Airport(270, 573), Cayo perico(114, 454)