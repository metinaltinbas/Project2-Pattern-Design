import random
from abc import *
from Room import *

class Ant:
    def __init__(self):
        self.x = 0
        self.y = 0
    
        
class Forager(Ant):
    def __init__(self,id,x,y):
        Ant.__init__(self)
        self.name = "Forager"
        self.id = id
        self.x = x
        self.y = y
        self.food = 0
        self.returnx = 0
        self.returny = 0
        self.antHillLife = 0
         
         

class Warrior(Ant):
    def __init__(self,id,x,y):
        Ant.__init__(self)
        self.name = "Warrior"
        self.id = id
        self.x = x
        self.y = y
        self.power = 12
    
   


# class SpeedBoost(Warrior):
   
#   def __init__(self,decorated_warrior):
#       Warrior.__init__(self,decorated_warrior)
   
#   def get_power(self):
#       return self.warrior.get_power() + 36
      
# class SecondChance(Warrior):
   
#   def __init__(self,decorated_warrior):
#       Warrior.__init__(self,decorated_warrior)
   
#   def get_power(self):
#       return self.warrior.get_power() + 12
      
# class OddsBoost(Warrior):
   
#   def __init__(self,decorated_warrior):
#       Warrior.__init__(self,decorated_warrior)
   
#   def get_power(self):
#       return self.warrior.get_power() + 24

      

class Worker(Ant):
    def __init__(self,id,x,y):
        Ant.__init__(self)
        self.name = "Worker"
        self.id = id
        self.x = x
        self.y = y
        self.antHillLife = 0
        