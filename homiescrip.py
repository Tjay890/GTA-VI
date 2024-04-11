from location import *
from player import *

class Crip(Location):
  def __init__(self, name, up, right, down, left, xcoord, ycoord):
    super().__init__(name, up, right, down, left, xcoord, ycoord)
  def enter(self):
    print("You are going inside.")
    self.homie()
  def homie(self):
    print("Tyrone: Yo wazzap homie.\nYou want to buy something?")
    print("Tyrone: ive got guns and joints")
    print("Tyrone: What do you want to buy:\n1. Guns\n2. Joints\n3. Nothing")
    #kies wat je wilt kopen
    choise = input()
    if choise == '1':
      self.gunna()
    elif choise == '2':
      self.joints()
    else:
      print("Aight i get it man. Money doesn't fall out the sky you know.")
      print("The same is with beautiful, big-titty, butt-naked women you know.")
  #regelt de shit die je koopt
  def gunna(self):
    print("Tyrone: I've got 2 guns:")
    print("1. Normal gun, 10k cash, 15-30 damage")
    print("2. RPG, 1m cash, 1000 damage")
    print("You currently have", player.cash, "cash.")
    gun = input("Tyrone: Which gun do you want to buy (1, 2, 3(none))\n")
    if gun == "1" and player.gunna is True or player.rpg is True and gun =="2":
      print("Tyrone: You've already got that")
    elif gun == '1' and player.cash >= 10000:
      player.cash -= 10000
      player.gunna = True
      print("Tyrone: You now have a Normal gun.")
      print("Tyrone: Good luck and have some fun with it.")
      print("You now have", player.cash, "cash.")
    elif gun == "2" and player.cash >= 1000000:
      player.cash -=1000000
      player.rpg = True
      print("Tyrone: You now have a RPG gun.")
      print("Tyrone: Good luck and have some fun with it.")
      print("You now have", player.cash, "cash.")
    elif gun == "3":
      print("Tyrone: No problem homie.")
    else:
      print("Tyrone: Looks like you a bit low on funds.")
      print("Tyrone: Come back when you have the money G.")
  def joints(self):
    print("Tyrone: The joints are 100 cash a piece")
    print("You currently have",player.cash,"cash.")
    print("Tyrone: How much joints do you want?")
    junta = int(input())
    if junta == 0:
      print("Tyrone: No promblem man.")
      print("Tyrone: Looks like i am boutta get high on ma own supply")
    elif player.cash >= junta*100:
      player.cash -= junta*100
      player.joints += junta
      print("Tyrone: Hope you enjoy it man.")
      print("You now have",player.joints,"joints.")
    else:
      print("Tyrone: You dont have the buying capacity.")