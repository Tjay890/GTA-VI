import wereld


# import locations.world 

# from pygame.constants import KEYDOWN

#game door Maarten, Jonathan en Tije
# pygame.init()
# bord = pygame.image.load("LS_Map(met lijntjes).jpg")
# WINDOW_SIZE= [800, 800]
# screen = pygame.display.set_mode(WINDOW_SIZE)
# pygame.display.set_caption("GTA VI(Leak)")
# done = False
# clock= pygame.time.Clock()

#while not done:
      #screen.fill((255,255,255))
      # bordrect = bord.get_rect()
      # screen.blit(bord, bordrect)
      # clock.tick(60)
      # pygame.display.flip()

      
# class Player():
#   pass

# class Item():
#   pass

# class Weapon(Item):
#   pass

# class Armor(Item):
#   pass




    
# house = House("House", "-", "-", "beach" , "homie's crip")
# beach = location("Beach", "house", "-", "-", "-")
# homiescrip = location("Homies crip", "nightclub", "freakshop", "barber", "house")
# nightclub = location("Nightclub", "-", "casino", "homie's crip", "-")

# current = house
# print(current)
# house.printdirections()
# house.move(current)


# world = {
#   "House" : {
#     "transitions": {
#       "down" : "Beach",
#       "right" : "homie's crip"
#     }
#   },
#   "Beach" : {
#     "transitions" : {
#       "up" : "House"
#     }
#   },
#   "Homie's crip" : {
#     "transitions" : {
#       "left" : "House",
#       "down" : "Barber",
#       "right" : "Freakshop",
#       "up" : "Nightclub"
#     }
#   },
#   "Nightclub" : {
#     "transitions" : {
#       "down" : "Homie's crip",
#       "right" : "Casino"
#     }
#   },
#   "Casino" : {
#     "transitions" : {
#       "left" : "Nightclub",
#       "down" : "Freakshop"
#     }
#   },
#   "Freakshop" : {
#     "transitions" : {
#       "left" : "Homie's crip",
#       "up" : "Casino"
#     }
#   },
#   "Barber" : {
#     "transitions" : {
#       "up" : "Homie's crip",
#       "down" : "Docks",
#       "left" : "Airport"
#     }
#   },
#   "Docks" : {
#     "transitions" : {
#       "up" : "Barber"
#     }
#   },
#   "Airport" : {
#     "transitions" : {
#       "right" : "Barber",
#       "left" : "Cayo perigo"
#     }
#   },
#   "cayo perigo" : {
#     "transitions" : {
#       "right" : "Airport"
#     }
#   }
# }

current = wereld.move("House")
while True:
  current = wereld.move(current)