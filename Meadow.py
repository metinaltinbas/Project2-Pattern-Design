from AntHill import *
# from Queen import *
import random

class Cell:
    def __init__(self):
        self.hill = None
        self.food = 0
        self.ants = []

        

class Meadow:
    def __init__(self):
        self.grid = [[0] * 20 for i in range(20)]
        # for i in range (3):
        #     builder = Queen()
        #     self.anthill = builder
        #     self.anthill.checkCordinates()
        self.anthillsList = []


    def setCell(self):
        for i in range(20):
            for k in range(20):
                a = Cell()
                self.grid[i][k] = a
                
                
    def randomFood(self):
        x = random.randint(0, 19)
        y = random.randint(0, 19)
        while self.grid[x][y].hill==1:
            x = random.randint(0, 19)
            y = random.randint(0, 19)
        self.grid[x][y].food +=1
            
 
                
    def create(self):
        for i in range(3):
            k = AntHill()
            k.checkCordinates(self.anthillsList)
            self.grid[k.x][k.y].hill = 1
            self.grid[k.x][k.y].food = 1
            for i in range(5):
                k.createAnts()
            # self.grid[k.x][k.y].ants.append(k.antList)
            self.anthillsList.append(k)
            
            
        
    def printU(self):
        
        print("======================")
        for i in range(len(self.anthillsList)):
            print("Colonie",i+1," in",self.anthillsList[i].x,self.anthillsList[i].y)
            for j in range(len(self.anthillsList[i].antList)):
                print((self.anthillsList[i].antList[j].name),(self.anthillsList[i].antList[j].x),(self.anthillsList[i].antList[j].y))
            print("======================")

        for i in range(20):
            for j in range(20):
                if self.grid[i][j].food != 0:
                    print ("food is here",i,j)

        for i in range(len(self.anthillsList)):
            forgnum = 0
            worknum = 0
            warionum = 0
            for j in range(len(self.anthillsList[i].antList)):
                if self.anthillsList[i].antList[j].name == "Warrior":
                    warionum += 1
                if self.anthillsList[i].antList[j].name == "Forager":
                    forgnum += 1
                if self.anthillsList[i].antList[j].name == "Worker":
                    worknum += 1

            print(
            "Colonie", i + 1, "in", self.anthillsList[i].x, self.anthillsList[i].y, " has", worknum, "  Worker ants",
            forgnum, "  Forager ants", warionum, "  Warrior ants")
            print("======================")
                    
        # for i in range(20):
        #     for j in range(20):
        #         print(self.grid[i][j].ants," Food:",self.grid[i][j].food," Cordinates",i,j)
        #     print("\n")
            
    def fight(self,ant1,ant2,j,k):
        if ant1.name=="Warrior" and ant2.name == "Forager": 
            if random.randint(0, 100) < 80:
                for i in range (len(self.anthillsList[ant2.id-1].antList)):
                    if self.anthillsList[ant2.id-1].antList[i] == ant2:
                        self.grid[ant2.x][ant2.y].ants.pop(0)
                        self.anthillsList[ant2.id-1].antList.pop(i)
                        print ("Warrior faced with Forager, Forager is dead.")
                        break

                
                # boost yapcaz.
                # ant1 = SpeedBoost(ant1)
                # print ("Power",ant1.power)
                pass
            else:
                print("Warrior faced with Forager, Forager escaped.")
                
        elif ant1.name=="Warrior" and ant2.name == "Warrior": 
            if ant1.power > ant2.power:
                for i in range (len(self.anthillsList[ant2.id-1].antList)):
                    if self.anthillsList[ant2.id-1].antList[i] == ant2:
                            self.grid[ant2.x][ant2.y].ants.pop(0)
                            self.anthillsList[ant2.id-1].antList.pop(i)
                            print ("2 Warriors faced, 2. Warrior dead")
                            break
            elif ant1.power == ant2.power:
                a=random.randint(0, 1)
                if a == 0:
                    for i in range (len(self.anthillsList[ant2.id-1].antList)):
                        if self.anthillsList[ant2.id-1].antList[i] == ant2:
                                self.grid[ant2.x][ant2.y].ants.pop(0)
                                self.anthillsList[ant2.id-1].antList.pop(i)
                                print ("2 Warriors faced, 2. Warrior dead")
                                break
                if a == 1:
                    for i in range (len(self.anthillsList[ant2.id-1].antList)):
                        if self.anthillsList[ant2.id-1].antList[i] == ant2:
                                self.grid[ant2.x][ant2.y].ants.pop(0)
                                self.anthillsList[ant2.id-1].antList.pop(i)
                                print ("2 Warriors faced, 1. Warrior dead")
                                break
                    # self.grid[ant2.x][ant2.y].ants.pop(0)
                    # self.anthillsList[ant1.id-1].antList.pop(j)
                    # print ("2 Warriors faced, 1. Warrior dead")
                    
            else:
                for i in range(len(self.anthillsList[ant2.id - 1].antList)):
                    if self.anthillsList[ant2.id - 1].antList[i] == ant2:
                        self.grid[ant2.x][ant2.y].ants.pop(0)
                        self.anthillsList[ant2.id - 1].antList.pop(i)
                        print ("2 Warriors faced, 1. Warrior dead")
                        break
                # self.grid[ant2.x][ant2.y].ants.pop(0)
                # self.anthillsList[ant1.id-1].antList.pop(j)
                # print ("2 Warriors faced, 1. Warrior dead")
                #
            
            pass
        else:
            if random.randint(0, 100) < 10:
                # self.grid[ant2.x][ant2.y].hill= None
                #
                # self.anthillsList.pop(ant1.id-1)
                print ("Warrior found hill, hill obliterated.")

            else:
                # self.grid[ant2.x][ant2.y].ants.pop(0)
                # self.anthillsList[ant1.id-1].antList.pop(j)
                print ("Warrior found hill, Warrior is dead.")



    def returnHill(self,ant1,returnAddress):
        # print(returnAddress)
        ant1.returnx = self.anthillsList[returnAddress-1].x
        ant1.returny = self.anthillsList[returnAddress-1].y
        # print("ben burdayim",ant1.returnx,ant1.returny)
        
        
    
    
    def cycle(self,choice):
        
        
        for turn in range(choice):
            
            if(len(self.anthillsList)>1):
                
                self.setCell()
                
                for foodTurn in range(15):
                    self.randomFood()
                
                
                for i in range(3):
                    j = 0
                    while(j < len(self.anthillsList[i].antList)):
                        if self.anthillsList[i].antList[j].name == "Warrior":
                            if(self.anthillsList[i].antList[j].x == 0 and self.anthillsList[i].antList[j].y == 0):
                                self.anthillsList[i].antList[j].x +=random.randint(0, 1)
                                self.anthillsList[i].antList[j].y +=random.randint(0, 1)
                                self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants.append(self.anthillsList[i].antList[j])
                                if(len(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants)>2):
                                    k = 0
                                    while(k<len(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants)):
                                        if(self.anthillsList[i].antList[j].id != self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].id):
                                            if(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].name =="Warrior"):
                                                print("iki warior",self.anthillsList[i].antList[j].x,self.anthillsList[i].antList[j].y,"Birinci",self.anthillsList[i].antList[j],self.anthillsList[i].antList[j].id,"Ikinci",self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k],self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].id)
                                                self.fight(self.anthillsList[i].antList[j] , self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k], j, k )
                                            elif(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].name =="Forager"):
                                                self.fight(self.anthillsList[i].antList[j] , self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k], j, k )
                                                print("bi warior bi forager",self.anthillsList[i].antList[j].x,self.anthillsList[i].antList[j].y)
                                            else:
                                                self.fight(self.anthillsList[i].antList[j] , self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k], j, k )
                                                print("bi warior bi hill")
                                                # self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].id
                                        k=k+1

                    
                                
                            elif(self.anthillsList[i].antList[j].x == 19 and self.anthillsList[i].antList[j].y == 19):
                                self.anthillsList[i].antList[j].x -=random.randint(0, 1)
                                self.anthillsList[i].antList[j].y -=random.randint(0, 1)
                                self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants.append(self.anthillsList[i].antList[j])
                                if(len(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants)>2):
                                    k = 0
                                    while (k < len(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants)):
                                        if(self.anthillsList[i].antList[j].id != self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].id):
                                            if(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].name =="Warrior"):
                                                print("iki warior",self.anthillsList[i].antList[j].x,self.anthillsList[i].antList[j].y,"Birinci",self.anthillsList[i].antList[j],self.anthillsList[i].antList[j].id,"Ikinci",self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k],self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].id)
                                                self.fight(self.anthillsList[i].antList[j] , self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k], j, k )

                                            elif(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].name =="Forager"):
                                                self.fight(self.anthillsList[i].antList[j] , self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k], j, k )
                                                print("bi warior bi forager",self.anthillsList[i].antList[j].x,self.anthillsList[i].antList[j].y)
                                            else:
                                                self.fight(self.anthillsList[i].antList[j] , self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k], j, k )
                                                print("bi warior bi hill")
                                                # self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].id
                                        k = k+1
                    
                                
                            
                            elif(self.anthillsList[i].antList[j].x == 0 and self.anthillsList[i].antList[j].y == 19):
                                self.anthillsList[i].antList[j].x +=random.randint(0, 1)
                                self.anthillsList[i].antList[j].y -=random.randint(0, 1)
                                self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants.append(self.anthillsList[i].antList[j])
                                if(len(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants)>2):
                                    k = 0
                                    while (k < len(self.grid[self.anthillsList[i].antList[j].x][ self.anthillsList[i].antList[j].y].ants)):
                                        if(self.anthillsList[i].antList[j].id != self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].id):
                                            if(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].name =="Warrior"):
                                                print("iki warior",self.anthillsList[i].antList[j].x,self.anthillsList[i].antList[j].y,"Birinci",self.anthillsList[i].antList[j],self.anthillsList[i].antList[j].id,"Ikinci",self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k],self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].id)
                                                self.fight(self.anthillsList[i].antList[j] , self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k], j, k )

                                            elif(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].name =="Forager"):
                                                self.fight(self.anthillsList[i].antList[j] , self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k], j, k )
                                                print("bi warior bi forager",self.anthillsList[i].antList[j].x,self.anthillsList[i].antList[j].y)
                                            else:
                                                self.fight(self.anthillsList[i].antList[j] , self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k], j, k )
                                                print("bi warior bi hill")
                                                # self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].id
                                        k = k+1
                    
                                
                            elif(self.anthillsList[i].antList[j].x == 19 and self.anthillsList[i].antList[j].y == 0):
                                self.anthillsList[i].antList[j].x -=random.randint(0, 1)
                                self.anthillsList[i].antList[j].y +=random.randint(0, 1)
                                self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants.append(self.anthillsList[i].antList[j])
                                if(len(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants)>2):
                                    k = 0
                                    while (k < len(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants)):
                                        if(self.anthillsList[i].antList[j].id != self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].id):
                                            if(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].name =="Warrior"):
                                                print("iki warior",self.anthillsList[i].antList[j].x,self.anthillsList[i].antList[j].y,"Birinci",self.anthillsList[i].antList[j],self.anthillsList[i].antList[j].id,"Ikinci",self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k],self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].id)
                                                self.fight(self.anthillsList[i].antList[j] , self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k], j, k )

                                            elif(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].name =="Forager"):
                                                self.fight(self.anthillsList[i].antList[j] , self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k], j, k )
                                                print("bi warior bi forager",self.anthillsList[i].antList[j].x,self.anthillsList[i].antList[j].y)
                                            else:
                                                self.fight(self.anthillsList[i].antList[j] , self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k], j, k )

                                                print("bi warior bi hill")
                                                # self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].id
                                        k = k+1
                    
                                
                            elif(self.anthillsList[i].antList[j].x == 0):
                                self.anthillsList[i].antList[j].x +=random.randint(0, 1)
                                y = random.randint(0, 1)
                                if y == 0:
                                    self.anthillsList[i].antList[j].y +=random.randint(0, 1)
                                else:
                                    self.anthillsList[i].antList[j].y -=random.randint(0, 1)
                                    
                                self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants.append(self.anthillsList[i].antList[j])
                                if(len(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants)>2):
                                    k = 0
                                    while (k < len(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants)):
                                        if(self.anthillsList[i].antList[j].id != self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].id):
                                            if(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].name =="Warrior"):
                                                print("iki warior",self.anthillsList[i].antList[j].x,self.anthillsList[i].antList[j].y,"Birinci",self.anthillsList[i].antList[j],self.anthillsList[i].antList[j].id,"Ikinci",self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k],self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].id)
                                                self.fight(self.anthillsList[i].antList[j] , self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k], j, k )

                                            elif(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].name =="Forager"):
                                                self.fight(self.anthillsList[i].antList[j] , self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k], j, k )
                                                print("bi warior bi forager",self.anthillsList[i].antList[j].x,self.anthillsList[i].antList[j].y)
                                            else:
                                                self.fight(self.anthillsList[i].antList[j] , self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k], j, k )

                                                print("bi warior bi hill")
                                        k = k+1        # self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].id
                                    
                    
                                    
                            elif(self.anthillsList[i].antList[j].x == 19):
                                self.anthillsList[i].antList[j].x -=random.randint(0, 1)
                                y = random.randint(0, 1)
                                if y == 0:
                                    self.anthillsList[i].antList[j].y +=random.randint(0, 1)
                                else:
                                    self.anthillsList[i].antList[j].y -=random.randint(0, 1)
                                
                                self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants.append(self.anthillsList[i].antList[j])
                                if(len(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants)>2):
                                    k = 0
                                    while (k < len(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants)):
                                        if(self.anthillsList[i].antList[j].id != self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].id):
                                            if(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].name =="Warrior"):
                                                print("iki warior",self.anthillsList[i].antList[j].x,self.anthillsList[i].antList[j].y,"Birinci",self.anthillsList[i].antList[j],self.anthillsList[i].antList[j].id,"Ikinci",self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k],self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].id)
                                                self.fight(self.anthillsList[i].antList[j] , self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k], j, k )

                                            elif(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].name =="Forager"):
                                                self.fight(self.anthillsList[i].antList[j] , self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k], j, k )
                                                print("bi warior bi forager",self.anthillsList[i].antList[j].x,self.anthillsList[i].antList[j].y)
                                            else:
                                                self.fight(self.anthillsList[i].antList[j] , self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k], j, k )
                                                print("bi warior bi hill")
                                        k = k+1        # self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].id
                                    
                    
                                
                                    
                            elif(self.anthillsList[i].antList[j].y == 19):
                                self.anthillsList[i].antList[j].y -=random.randint(0, 1)
                                y = random.randint(0, 1)
                                if y == 0:
                                    self.anthillsList[i].antList[j].x +=random.randint(0, 1)
                                else:
                                    self.anthillsList[i].antList[j].x -=random.randint(0, 1)
                                    
                                self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants.append(self.anthillsList[i].antList[j])
                                if(len(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants)>2):
                                    k = 0
                                    while (k < len(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants)):
                                        if(self.anthillsList[i].antList[j].id != self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].id):
                                            if(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].name =="Warrior"):
                                                print("iki warior",self.anthillsList[i].antList[j].x,self.anthillsList[i].antList[j].y,"Birinci",self.anthillsList[i].antList[j],self.anthillsList[i].antList[j].id,"Ikinci",self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k],self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].id)
                                                self.fight(self.anthillsList[i].antList[j] , self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k], j, k )

                                            elif(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].name =="Forager"):
                                                self.fight(self.anthillsList[i].antList[j] , self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k], j, k )
                                                print("bi warior bi forager",self.anthillsList[i].antList[j].x,self.anthillsList[i].antList[j].y)
                                            else:
                                                self.fight(self.anthillsList[i].antList[j] , self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k], j, k )

                                                print("bi warior bi hill")
                                                # self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].id
                                        k = k+1
                    
                                    
                            elif(self.anthillsList[i].antList[j].y == 0):
                                self.anthillsList[i].antList[j].y +=random.randint(0, 1)
                                y = random.randint(0, 1)
                                if y == 0:
                                    self.anthillsList[i].antList[j].x +=random.randint(0, 1)
                                else:
                                    self.anthillsList[i].antList[j].x -=random.randint(0, 1)
                                    
                                self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants.append(self.anthillsList[i].antList[j])
                                if(len(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants)>2):
                                    k = 0
                                    while (k < len(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants)):
                                        if(self.anthillsList[i].antList[j].id != self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].id):
                                            if(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].name =="Warrior"):
                                                print("iki warior",self.anthillsList[i].antList[j].x,self.anthillsList[i].antList[j].y,"Birinci",self.anthillsList[i].antList[j],self.anthillsList[i].antList[j].id,"Ikinci",self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k],self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].id)
                                                self.fight(self.anthillsList[i].antList[j] , self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k], j, k )

                                            elif(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].name =="Forager"):
                                                self.fight(self.anthillsList[i].antList[j] , self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k], j, k )
                                                print("bi warior bi forager",self.anthillsList[i].antList[j].x,self.anthillsList[i].antList[j].y)
                                            else:
                                                self.fight(self.anthillsList[i].antList[j] , self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k], j, k )

                                                print("bi warior bi hill")
                                        k = k+1        # self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].id

                    
                                    
                            else:
                                t = random.randint(0, 1)
                                if t == 0:
                                    y = random.randint(0, 1)
                                    if y == 0:
                                        self.anthillsList[i].antList[j].y +=random.randint(0, 1)
                                    else:
                                        self.anthillsList[i].antList[j].y -=random.randint(0, 1)
                                    self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants.append(self.anthillsList[i].antList[j])
                                    if(len(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants)>2):
                                        k = 0
                                        while (k < len(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants)):
                                            if(self.anthillsList[i].antList[j].id != self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].id):
                                                if(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].name =="Warrior"):
                                                    print("iki warior",self.anthillsList[i].antList[j].x,self.anthillsList[i].antList[j].y,"Birinci",self.anthillsList[i].antList[j],self.anthillsList[i].antList[j].id,"Ikinci",self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k],self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].id)
                                                    self.fight(self.anthillsList[i].antList[j] , self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k], j, k )

                                                elif(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].name =="Forager"):
                                                    self.fight(self.anthillsList[i].antList[j] , self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k], j, k )
                                                    print("bi warior bi forager",self.anthillsList[i].antList[j].x,self.anthillsList[i].antList[j].y)
                                                else:
                                                    self.fight(self.anthillsList[i].antList[j] , self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k], j, k )

                                                    print("bi warior bi hill")
                                            k = k+1       # self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].id
                                    
                    
                                else:
                                    x = random.randint(0, 1)
                                    if x == 0:
                                        self.anthillsList[i].antList[j].x +=random.randint(0, 1)
                                    else:
                                        self.anthillsList[i].antList[j].x -=random.randint(0, 1)
                                     
                                    self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants.append(self.anthillsList[i].antList[j])
                                    if(len(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants)>2):
                                        k = 0
                                        while (k < len(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants)):
                                            if(self.anthillsList[i].antList[j].id != self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].id):
                                                if(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].name =="Warrior"):
                                                    print("iki warior",self.anthillsList[i].antList[j].x,self.anthillsList[i].antList[j].y,"Birinci",self.anthillsList[i].antList[j],self.anthillsList[i].antList[j].id,"Ikinci",self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k],self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].id)
                                                    self.fight(self.anthillsList[i].antList[j] , self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k], j, k )

                                                elif(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].name =="Forager"):
                                                    self.fight(self.anthillsList[i].antList[j] , self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k], j, k )
                                                    print("bi warior bi forager",self.anthillsList[i].antList[j].x,self.anthillsList[i].antList[j].y)
                                                else:
                                                    self.fight(self.anthillsList[i].antList[j] , self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k], j, k )

                                                    print("bi warior bi hill")
                                                    # self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].id
                                            k = k+1

                                    
                                
                                    
                        elif self.anthillsList[i].antList[j].name == "Forager":
                            
                            if self.anthillsList[i].antList[j].food !=1:
                            
                                if(self.anthillsList[i].antList[j].x == 0 and self.anthillsList[i].antList[j].y == 0):
                                    self.anthillsList[i].antList[j].x +=random.randint(0, 1)
                                    self.anthillsList[i].antList[j].y +=random.randint(0, 1)
                                    self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants.append(self.anthillsList[i].antList[j])
                                    for k in range(len(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants)):
                                        if (self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].food == 1 and self.anthillsList[i].antList[j].id != self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].id ):
                                            print("yemek",(self.anthillsList[i].antList[j].x),(self.anthillsList[i].antList[j].y))
                                            self.anthillsList[i].antList[j].food=1
                                            self.returnHill(self.anthillsList[i].antList[j],self.anthillsList[i].antList[j].id)

                                elif(self.anthillsList[i].antList[j].x == 19 and self.anthillsList[i].antList[j].y == 19):
                                    self.anthillsList[i].antList[j].x -=random.randint(0, 1)
                                    self.anthillsList[i].antList[j].y -=random.randint(0, 1)
                                    self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants.append(self.anthillsList[i].antList[j])
                                    for k in range(len(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants)):
                                        if (self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].food == 1 and self.anthillsList[i].antList[j].id != self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].id ):
                                            print("yemek",(self.anthillsList[i].antList[j].x),(self.anthillsList[i].antList[j].y))
                                            self.anthillsList[i].antList[j].food=1
                                            self.returnHill(self.anthillsList[i].antList[j],self.anthillsList[i].antList[j].id)
                                
                                elif(self.anthillsList[i].antList[j].x == 0 and self.anthillsList[i].antList[j].y == 19):
                                    self.anthillsList[i].antList[j].x +=random.randint(0, 1)
                                    self.anthillsList[i].antList[j].y -=random.randint(0, 1)
                                    self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants.append(self.anthillsList[i].antList[j])
                                    for k in range(len(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants)):
                                        if (self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].food == 1 and self.anthillsList[i].antList[j].id != self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].id ):
                                            print("yemek",(self.anthillsList[i].antList[j].x),(self.anthillsList[i].antList[j].y))
                                            self.anthillsList[i].antList[j].food=1
                                            self.returnHill(self.anthillsList[i].antList[j],self.anthillsList[i].antList[j].id)
                                    
                                elif(self.anthillsList[i].antList[j].x == 19 and self.anthillsList[i].antList[j].y == 0):
                                    self.anthillsList[i].antList[j].x -=random.randint(0, 1)
                                    self.anthillsList[i].antList[j].y +=random.randint(0, 1)
                                    self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants.append(self.anthillsList[i].antList[j])
                                    for k in range(len(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants)):
                                        if (self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].food == 1 and self.anthillsList[i].antList[j].id != self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].id ):
                                            print("yemek",(self.anthillsList[i].antList[j].x),(self.anthillsList[i].antList[j].y))
                                            self.anthillsList[i].antList[j].food=1
                                            self.returnHill(self.anthillsList[i].antList[j],self.anthillsList[i].antList[j].id)
                                    
                                elif(self.anthillsList[i].antList[j].x == 0):
                                    self.anthillsList[i].antList[j].x +=random.randint(0, 1)
                                    y = random.randint(0, 1)
                                    if y == 0:
                                        self.anthillsList[i].antList[j].y +=random.randint(0, 1)
                                    else:
                                        self.anthillsList[i].antList[j].y -=random.randint(0, 1)
                                    
                                    self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants.append(self.anthillsList[i].antList[j])
                                    for k in range(len(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants)):
                                        if (self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].food == 1 and self.anthillsList[i].antList[j].id != self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].id ):
                                            print("yemek",(self.anthillsList[i].antList[j].x),(self.anthillsList[i].antList[j].y))
                                            self.anthillsList[i].antList[j].food=1
                                            self.returnHill(self.anthillsList[i].antList[j],self.anthillsList[i].antList[j].id)
                                        
                                elif(self.anthillsList[i].antList[j].x == 19):
                                    self.anthillsList[i].antList[j].x -=random.randint(0, 1)
                                    y = random.randint(0, 1)
                                    if y == 0:
                                        self.anthillsList[i].antList[j].y +=random.randint(0, 1)
                                    else:
                                        self.anthillsList[i].antList[j].y -=random.randint(0, 1)
                                    
                                    self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants.append(self.anthillsList[i].antList[j])
                                    for k in range(len(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants)):
                                        if (self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].food == 1 and self.anthillsList[i].antList[j].id != self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].id ):
                                            print("yemek",(self.anthillsList[i].antList[j].x),(self.anthillsList[i].antList[j].y))
                                            self.anthillsList[i].antList[j].food=1
                                            self.returnHill(self.anthillsList[i].antList[j],self.anthillsList[i].antList[j].id)
                                        
                                elif(self.anthillsList[i].antList[j].y == 19):
                                    self.anthillsList[i].antList[j].y -=random.randint(0, 1)
                                    y = random.randint(0, 1)
                                    if y == 0:
                                        self.anthillsList[i].antList[j].x +=random.randint(0, 1)
                                    else:
                                        self.anthillsList[i].antList[j].x -=random.randint(0, 1)
                                    
                                    self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants.append(self.anthillsList[i].antList[j])
                                    for k in range(len(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants)):
                                        if (self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].food == 1 and self.anthillsList[i].antList[j].id != self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].id ):
                                            print("yemek",(self.anthillsList[i].antList[j].x),(self.anthillsList[i].antList[j].y))
                                            self.anthillsList[i].antList[j].food=1
                                            self.returnHill(self.anthillsList[i].antList[j],self.anthillsList[i].antList[j].id)
                                        
                                elif(self.anthillsList[i].antList[j].y == 0):
                                    self.anthillsList[i].antList[j].y +=random.randint(0, 1)
                                    y = random.randint(0, 1)
                                    if y == 0:
                                        self.anthillsList[i].antList[j].x +=random.randint(0, 1)
                                    else:
                                        self.anthillsList[i].antList[j].x -=random.randint(0, 1)
                                    
                                    self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants.append(self.anthillsList[i].antList[j])
                                    for k in range(len(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants)):
                                        if (self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].food == 1 and self.anthillsList[i].antList[j].id != self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].id ):
                                            print("yemek",(self.anthillsList[i].antList[j].x),(self.anthillsList[i].antList[j].y))
                                            self.anthillsList[i].antList[j].food=1
                                            self.returnHill(self.anthillsList[i].antList[j],self.anthillsList[i].antList[j].id)
                                        
                                else:
                                    t = random.randint(0, 1)
                                    if t == 0:
                                        y = random.randint(0, 1)
                                        if y == 0:
                                            self.anthillsList[i].antList[j].y +=random.randint(0, 1)
                                        else:
                                            self.anthillsList[i].antList[j].y -=random.randint(0, 1)
                                        self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants.append(self.anthillsList[i].antList[j])    
                                    else:
                                        x = random.randint(0, 1)
                                        if x == 0:
                                            self.anthillsList[i].antList[j].x +=random.randint(0, 1)
                                        else:
                                            self.anthillsList[i].antList[j].x -=random.randint(0, 1)
                                         
                                        self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants.append(self.anthillsList[i].antList[j])    
                                    for k in range(len(self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants)):
                                        if (self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].food == 1 and self.anthillsList[i].antList[j].id != self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants[k].id ):
                                            print("yemek",(self.anthillsList[i].antList[j].x),(self.anthillsList[i].antList[j].y))
                                            self.anthillsList[i].antList[j].food=1
                                            self.returnHill(self.anthillsList[i].antList[j],self.anthillsList[i].antList[j].id)
                                
                            else:
                                # print ("geri donus rotasi")
                                if (self.anthillsList[i].antList[j].x > self.anthillsList[i].antList[j].returnx):
                                    self.anthillsList[i].antList[j].x -=1
                                    self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants.append(self.anthillsList[i].antList[j])
                                elif (self.anthillsList[i].antList[j].x < self.anthillsList[i].antList[j].returnx):
                                    self.anthillsList[i].antList[j].x +=1
                                else:
                                    if (self.anthillsList[i].antList[j].y > self.anthillsList[i].antList[j].returny):
                                        self.anthillsList[i].antList[j].y -=1
                                        self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants.append(self.anthillsList[i].antList[j])
                                    elif (self.anthillsList[i].antList[j].y < self.anthillsList[i].antList[j].returny):
                                        self.anthillsList[i].antList[j].y +=1
                                        self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants.append(self.anthillsList[i].antList[j])
                                    else:
                                        self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].food += 1
                                        self.anthillsList[i].antList[j].food = 0
                                    
                                        
                        else:
                            self.grid[self.anthillsList[i].antList[j].x][self.anthillsList[i].antList[j].y].ants.append(self.anthillsList[i].antList[j])
                            for crearteTurn in range(3):
                                if self.anthillsList[crearteTurn].totNum < 20:
                                    if self.anthillsList[crearteTurn].workerNum < len(self.anthillsList[crearteTurn].roomList):
                                        # print("worker sayisi kadar karinca",self.anthillsList[i].workerNum)
                                        # print(self.anthillsList[i])
                                        for j in range(self.anthillsList[crearteTurn].workerNum):
                                            self.anthillsList[crearteTurn].createAnts()
                                        # worker sayisi kadar karinca
                                    if self.anthillsList[crearteTurn].workerNum > len(self.anthillsList[crearteTurn].roomList):
                                        # print("room sayisi kadar karinca ureticez")
                                        # room sayisi kadar karinca ureticez
                                        for j in range(self.anthillsList[crearteTurn].roomList):
                                            self.anthillsList[crearteTurn].createAnts()
                            # print("workerlar room yapicak")
                        j = j+1
                self.printU()
                print("======Turn======")