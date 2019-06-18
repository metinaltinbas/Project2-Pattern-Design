import random
# from Ant import *
from Room import *

class AntHill:
    counter = 1 
    def __init__(self):
        self.x = random.randint(0, 19)
        self.y = random.randint(0, 19)
        self.name = "anthill"
        self.id = self.__class__.counter
        self.__class__.counter += 1
        self.antList = []
        self.roomList = []
        self.workerNum = 0
        self.totNum = 0
        self.life = 0

    def checkCordinates(self,list):
        for i in range(len(list)):
           while self.x == list[i].x:
               x = random.randint(0, 19)
               self.x = x
        for i in range(len(list)):
        	while self.y == list[i].y:
        		y = random.randint(0, 19)
        		self.y = y
		
    def createAnts(self):
        roomType = random.randint(0, 2)
        ants = AntFactory()
        if roomType == 0:
            self.workerNum += 1
        ants.createAnt(roomType,self.antList,self.id,self.x,self.y)
        self.totNum +=1
        self.roomList.append(ants)
        
        

        
        