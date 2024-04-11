from location import *
from player import *
import time

class Freakshop(Location):
  def __init__(self, name, up, right, down, left, xcoord, ycoord):
    super().__init__(name, up, right, down, left, xcoord, ycoord)


  
  def enter(self):
    #zorgt ervoor dat je naar binnen gaat
    print("Press enter to enter the freakshop!")
    input()
    self.story()
  
  
  def story(self):
    #checkt of je crowbar en een driver hebt en past het verhaal daarop aan
    if player.crowbar >= 1 and player.driver != 'No one':
      print("Pablo: So you got the crowbar.\n Go to the docks and open a container.")
      print("Pablo: Yo driver will wait there with the getaway car.")
      print("---------------------------------")
    elif player.crowbar >= 1:
      print("Pablo: Looks like you have got a crowbar.")
      print("Pablo: You can do a heist with that crowbar.")
      print("Pablo: Here, let me expalain.")
      #gaat naar driver kiezen
      self.chosing()
    else:
      print("Pablo: Yo man what up?")
      input("DeMarcus: ")
      print("Pablo: Who asked.")
      time.sleep(2)
      print("Pablo: Just kidding.")
      print("Pablo: Here at the freakshop we plan heists.")
      print("Pablo: But before i tell you more you have to say if you are in.")
      print("Pablo: So, you in?")
      input("DeMarcus: ")
      print("Pablo: You have no choice man!")
      print("Pablo: Let's begin!")
      print("---------------------------------")
      #gaat naar driver kiezen
      self.chosing()

  def chosing(self):
    print("Pablo: First you have to chose yo crew man")
    print("Pablo: Chose wisely, yo ass may get scammed!!")
    print("---------------------------------")
    print ("Chose the driver:\n 1:Rashid\n 2:Mo\n 3:Jayquavion")
    #kiest je driver voor de heist
    player.driver = input(">")
    print("Ai, wise choise amigo!")
    print("---------------------------------")
    self.startheist()


#starting the heist
  def startheist(self):
    print("Now you need a crowbar.\n You can find one at the beach.")
    print("Once you have the crowbar, comeback.")
    input("Press enter to leave")



   
    
    