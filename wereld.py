#importeert alle bestanden die nodig zijn
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
from player import *

current = "House"
#de wereld met alle bestemmingen
# "locatie": class("Naam huidige locatie","Boven","Rechts", "Beneden", "Links", xcoordinaat op de map, Ycoordinaat op de map)
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
  #zorgt dat huidige plek wordt gebruikt voor locaties laten zien
  objHere = world[current]
  objHere.printdirections()
  #Kijkt welke toets je in drukt om daarna te gaan verwerken
  direction = getkey()
  #Behandelt wat er gebeurt als je op een toets drukt.
  #Boven
  if direction == keys.UP:
    #kijkt of plek waar je naartoe gaat niet leeg is. Is bij de andere ook zo
    if objHere.up != "-":
      #zorgt dat current wordt wat er in de dictionary bij up staat
      current = objHere.up
    else:
      print("There is nothing there.")
  #Rechts
  elif direction == keys.RIGHT:
    if objHere.right != "-":
      current = objHere.right
    else:
      print("There is nothing there.")
  #Onder
  elif direction == keys.DOWN:
    if objHere.down != "-":
      current = objHere.down
    else:
      print("There is nothing there.")
  #Links
  elif direction == keys.LEFT:
    if objHere.left != "-":
      current = objHere.left
    else:
      print("There is nothing there.")
  #voor naar binnen gaan bij die plek en dat roept de fuctie enter aan van die huidige plek
  elif direction == keys.ENTER:
    objHere.enter()
  #laat de inventory zien
  elif direction == keys.I:
    #welk haar je hebt
    print("Your haircut is", player.hair)
    #kijkt welke driver je hebt gekozen
    if player.driver == "1":
      print("Your driver is Rashid.")
    elif player.driver == "2":
      print("Your driver is Mo.")
    elif player.driver == "3":
      print("Your driver is Jayquavion")
    elif player.driver == "No one":
      print("You have no driver.")
    else:
      print("Your driver is", player.driver)
    #checkt je ticket voor cayo perico
    if player.ticket is False:
      print("You dont have a ticket to cayo perico.")     
    elif player.ticket is True:
      print("You have a ticket to cayo perico.")
    else:
      print("Something is wrong here")
    # laat zien hoeveel cash en joints je hebt
    print("You have",player.joints,"joints and",player.cash,"cash")
    #Laat zien of je een gun hebt
    if player.gunna is True:
      print("You have a gun.")
    else:
      print("You dont have a gun")
    #laat zien of je een rpg hebt
    if player.rpg is True:
      print("You have a RPG")
    else:
      print("You dont have a RPG")
    #laat de overige items zien in je inventory
    print("You have these items in your inventory:\n",player.inventory)
    print()
  #voor als je geen juiste actie uitvoert
  else:
    print("You can't go there!")
  #Checkt of je naar cayo perico probeert te gaan zonder dat je een ticket hebt
  if current == "Cayo perico" and player.ticket is False:
    print("You haven't unlocked this area yet.")
    print("Buy a ticket at the airport and then you can come back to cayo perico.")
    print()
    #stuurt je terug naar de airport
    current = "Airport"
  #geeft aan main.py terug wat current moet zijn  
  return current