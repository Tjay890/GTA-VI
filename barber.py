from location import *




class Haircut:
  
  def hairstyle(hair):
    print("Do want a haircut ma G?\nYou aint looking fresh with that",hair,"!")
    a = input(">")
    if a.lower() == "no":
      hair = "YEYEASSHAIRCUT"
      print("Yo hairstyle is now", hair, "N***a!")
      return hair
    else:
      print("Wich haircut do you want ma n***a!")
      print("You can chose between these 5 n***a!")
      print("Buzz, Fringe, Mullet, Bold or Default")
      hair = str(input(">"))
      while (hair != "Buzz" and hair != "Fringe" and hair != "Mullet"
             and hair != "Bold" and hair != "Default"):
        print("You cannot chose that n***a !\nChoose again!")
        print("")
        print("Wich haircut do you want ma n***a!")
        print("You can chose between these 5 n***a!")
        print("Buzz, Fringe, Mullet, Bold or Default")
        hair = str(input(">"))
      print("Yo hairstyle is now", hair, "N***a!")
      print("")
      return hair
  


class Barber(Location):
  hair = "YEYEASSHAIRCUT"
  def __init__(self, name, up, right, down, left, xcoord, ycoord):
    super().__init__(name, up, right, down, left, xcoord, ycoord)

  def enter(self):
    print("You are going inside.")
    self.hair = Haircut.hairstyle(self.hair)
    
