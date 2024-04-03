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
  else:
    print("You can't go there!")
  return current

current = "House"
world = {
  "House": House("House","-","Homie's crip", "Beach", "-"),
  "Beach": Beach("Beach","House", "-", "-", "-"),
  "Homie's crip": Crip("Homie's crip","Nightclub","Freakshop", "Barber", "House"),
  "Nightclub": Nightclub("Nightclub","-","Casino", "Homie's crip", "-"),
  "Casino": Casino("Casino","-","-", "Freakshop", "Nightclub"),
  "Freakshop": Freakshop("Freakshop","Casino","-", "-", "Homie's crip"),
  "Barber": Barber("Barber","Homie's crip","-", "Docks", "Airport"),
  "Docks": Docks("Docks","Barber","-", "-", "-"),
  "Airport": Airport("Airport","-","Barber", "-", "Cayo perico"),
  "Cayo perico": Cayo("Cayo perico","-","Airport", "-", "-")
}