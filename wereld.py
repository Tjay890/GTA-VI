from getkey import getkey, keys
from house import *
from beach import *
from airport import *
from barber import *
from casino import *
from cayoperico import *
from docks import *
from freakshop import *
from homiescrip import *
from nightclub import *

current = "House"
world = {
  "House": House("House","-","Homie's crip", "Beach", "-",234, 262),
  "Beach": Beach("Beach","House", "-", "-", "-",188, 369),
  "Homie's crip": Crip("Homie's crip","Nightclub","Freakshop", "Barber", "House",392, 318),
  "Nightclub": Nightclub("Nightclub","-","Casino", "Homie's crip", "-",436, 184),
  "Casino": Casino("Casino","-","-", "Freakshop", "Nightclub",546, 200),
  "Freakshop": Freakshop("Freakshop","Casino","-", "-", "Homie's crip",501, 279),
  "Barber": Barber("Barber","Homie's crip","-", "Docks", "Airport",439, 450),
  "Docks": Docks("Docks","Barber","-", "-", "-",556, 662),
  "Airport": Airport("Airport","-","Barber", "-", "Cayo perico",270, 573),
  "Cayo perico": Cayo("Cayo perico","-","Airport", "-", "-",114, 454)
}

def move(current):
  objHere = world[current]
  objHere.printdirections()
  direction = getkey()
  print(direction)
  
  if direction == keys.UP:
    if objHere.up != "-":
      # current.exit()
      current = objHere.up
      # current.entry()
  elif direction == keys.RIGHT:
    if objHere.right != "-":
      current = objHere.right
  elif direction == keys.DOWN:
    if objHere.down != "-":
      current = objHere.down
  elif direction == keys.LEFT:
    if objHere.left != "-":
      current = objHere.left
  elif direction == keys.ENTER:
    objHere.enter()
  else:
    print("You can't go there!")
  return current

