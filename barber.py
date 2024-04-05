from location import *


class haircut:

  def hairstyle():
    print("Do want a haircut ma G?")
    a = input(">")
    if a == "No" or a == "no":
      style = "YEYEASSHAIRCUT"
      return style
    else:
      print("Wich haircut do you want ma n***a!")
      print("You can chose between these 5 n***a!")
      print("Buzz, Fringe, Mullet, Bold or Default")
      hair = str(input(">"))
      while (hair != "Buzz" and hair != "Fringe" and hair != "Mullet"
             and hair != "Bold" and hair != "Default"):
        print("You cannot chose that n***a !\nChoose again!")
        print("Wich haircut do you want ma n***a!")
        print("You can chose between these 5 n***a!")
        print("Buzz, Fringe, Mullet, Bold or Default")
        hair = str(input(">"))
      return hair

  hairthing = hairstyle()
  print("Yo hairstyle is now", hairthing, "N***a!")


class Barber(Location):

  def __init__(self, name, up, right, down, left):
    super().__init__(name, up, right, down, left)
