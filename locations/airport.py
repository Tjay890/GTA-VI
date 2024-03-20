from location import *

class Airport(Location):
  def __init__(self, name, up, right, down, left):
    super().__init__(name, up, right, down, left)