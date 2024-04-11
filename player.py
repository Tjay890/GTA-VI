import random

class Stats:
  joints1 = 0
  gun1 = False
  cash = 100
  rpg1 = False
  def __init__(self, health = 80, power = 15):
    self.life = health
    self.damage = power

  def attack(self):
    print("You got popped!")
    damage = random.randint(0, self.damage)
    print("Damage:", damage)
    player.life -= damage

  def healthcheck(self):
    if self.life > 0:
      print("Enemy health is:", self.life)
    else:
      print("Enemy's ass is dead G!")






class Player(Stats):
  ticket = False
  joints = Stats.joints1
  gunna = Stats.gun1
  rpg = Stats.rpg1
  freejoints = False
  def __init__(self, health = 100, power = 20):
    Stats.__init__(self, health = 80, power = 15)


  def punch(self):
    print("You did a punch attack.")
    damage = random.randint(0, self.damage)
    print("Damage:", damage)
    Boss1.life -= damage


  def kick(self):
    print("You did a kick attack.")
    if random.randint(0, 1) == 0:
      damage = random.randint(10, 25)
      print("Damage:", damage)
      Boss1.life -= damage
    else:
      print("Yo ass missed the kick")


  def gun(self):
    print("You choses the gun.")
    if self.gunna is True:
      damage = random.randint(15, 30)
      print("Damage:", damage)
      Boss1.life -= damage
    else:
      print("You have not unlocked the gun.")

  def rocketlauncher(self):
    print("You have chosen the ultimute rocketlauncher")
    if self.rpg is True:
      damage = 1000
      print("Damage:", damage)
      Boss1.life -= damage
    else:
      print("You have not unlocked the rocketlauncher")



  def healthcheck(self):
    if self.life > 0:
      print("your health is:", self.life)
    else:
      print("Yoo ass is dead G!")


  def heal(self):
    if self.joints >= 1:
      self.life += 5
      print("You got yo self healed")
      print("Yo health is:", self.life)
      self.joints -= 1
    else:
      print("Yo ass already has enough joints man!")


player = Player()
Boss1 = Stats()



# while player.life >= 0 and Boss1.life >= 0:
#   print("chose your strategy")
#   print("1:punch")
#   print("2:kick")
#   print("3:gun")
#   print("4:rocketlauncher")
#   print("5:heal")
#   attack = input(">")
#   if attack == "1":
#     player.punch()
#   elif attack == "2":
#     player.kick()
#   elif attack == "3":
#     player.gun()
#   elif attack == "4":
#     player.rocketlauncher()
#   elif attack == "5":
#     player.heal()
#   else:
#     print("You can not do that.")

#   print("----------------------")
#   Boss1.healthcheck()
#   player.healthcheck()
#   print("----------------------")
#   if player.life >= 0 and Boss1.life >= 0:
#     Boss1.attack()
#     player.healthcheck()
#     print("----------------------")

# if Boss1.life > 0:
#   print("El Rubio has won with ", Boss1.life, "lifes.")
# else:
#   print(" Demarcus has won with ", player.life, "lifes.")

