from house import *
from kitchen import *
def move(current):
  objHere = world[current]
  objHere.printdirections()
  direction = input("Where do you want to go? ")
  
  if direction == "up":
    if objHere.up != "-":
      # current.exit()
      current = objHere.up
      # current.entry()
  elif direction == "right":
    if objHere.right != "-":
      current = objHere.right
  elif direction == "down":
    if objHere.down != "-":
      current = objHere.down
  elif direction == "left":
    if objHere.left != "-":
      current = objHere.left
  else:
    print("You can't go there!")
  return current

current = "House"
world = {
  "House": House("House","Kitchen","-", "-", "-"),
  "Kitchen": Kitchen("Kitchen","-", "-", "House", "-")
}