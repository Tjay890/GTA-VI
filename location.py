class Location():
  def __init__(self, name, up, right ,down, left, xcoord, ycoord):
    self.name = name
    self.up = up
    self.right = right
    self.down = down
    self.left = left
    self.x = xcoord
    self.y = ycoord
  #laat zien wat de speler kan doen
  def printdirections(self):
    print("You are currently at " + self.name)
    print()
    print("You can view your inventory by pressing [I],")
    print("You can enter this place by pressing [ENTER] or,")
    print("You can go:\n", "Up:",self.up,"\n","Right:",self.right,"\n","Down:",self.down,"\n","Left:",self.left)
  def enter(self):
    print("There is nothing to do here.(Press enter)")
    input()
  