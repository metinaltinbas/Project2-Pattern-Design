from Meadow import *


def main():
    # y = AntHill()
    # x = AntFactory()
    # x.createAnt(y)
    # Worker ants die when they create a room (1 points) When a warrior wins a fight, it gains some attribute decorator (5 points) Anthills are spawned during initialization using Builder pattern
    # Creating new rooms cost 1 food and kills the worker (3 points) 
    pass

if(__name__ == "__main__"):
    main()
    
    nCycle = int(input("How many cycle: "))
    y = Meadow()
    y.setCell()
    y.create()
    
    y.cycle(nCycle)
    y.printU()
    