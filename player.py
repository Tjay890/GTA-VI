#Player stats
import random

cookies1 = 0
gun1 = 0
cash = 0


class Stats:

  
  def __init__(self, health = 80, power = 15):
    self.life = health
    self.damage = power

  def attack(self):
    print("You got popped!")
    damage = random.randint(0, self.damage)
    print("Damage:", damage)

  def healthcheck(self):
    if self.life >= 0:
      print("Yo health is:", self.life)
    else:
      print("Yoo ass is dead G!")






class Player(Stats):

  cookies = cookies1
  gunna = gun1
  
  def __init__(self, health = 100, power = 20):
    Stats.__init__(self, health = 80, power = 15)


  def punch(self):
    print("You did a punch attack.")
    damage = random.randint(0, self.damage)
    print("Damage:", damage)

  
  def kick(self):
    print("You did a kick attack.")
    if random.randint(0, 1) == 0:
      damage = random.randint(10, 25)
      print("Damage:", damage)
    else:
      print("Yo ass missed the kick")
    

  def gun(self):
    print("You choses the gun.")
    if self.gunna >= 1:
      damage = random.randint(15, 30)
      print("Damage:", damage)
    
    
  def healthcheck(self):
    Stats.healthcheck(self)

  def heal(self):
    if self.cookies >= 1:
      self.life += 5
      print("You got yo self healed")
      print("Yo health is:", self.life)
      self.cookies -= 1
    else:
      print("Yo ass already has enough cookies man!")
      

player = Player()
Boss1 = Stats()