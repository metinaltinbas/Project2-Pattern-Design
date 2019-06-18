from Ant import *
import random
import abc


class AntFactory:
    def createAnt(self,type,list,id,x,y):
        if type == 0: 
            return WorkerRoom(list,id,x,y)
        if type == 1: 
            return ForagerRoom(list,id,x,y)
        if type == 2: 
            return WarriorRoom(list,id,x,y)
            
    @abc.abstractmethod
    def _factory_method(self):
        pass
        

class WorkerRoom(AntFactory):
    def __init__(self,list,id,x,y):
        w = Worker(id,x,y)
        list.append(w)
        print ('worker room')

    
class ForagerRoom(AntFactory):
    def __init__(self,list,id,x,y):
        f = Forager(id,x,y)
        list.append(f)
        print ('forager room')
    
class WarriorRoom(AntFactory):
    def __init__(self,list,id,x,y):
        war = Warrior(id,x,y)
        list.append(war)
        print ('warrior room')
    

        
    