class Location():
  def __init__(self, name, up, right ,down, left):
    self.name = name
    self.up = up
    self.right = right
    self.down = down
    self.left = left
  def printdirections(self):
    print("You are currently at " + self.name)
    print("You can go:\n", "Up:",self.up,"\n","Right:",self.right,"\n","Down:",self.down,"\n","Left:",self.left)
  