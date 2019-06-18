# CS342 Design Patterns
## Fall 2018
### PROJECT 2 README FILE

## DESIGN OVERVIEW:
- We have created our grid with cell objects in it and set food , antlists and hills as a attribute to cell object.
- Created fight function to let ants fight with each other
- We check whether anthill has 20 ants or less when we create ants.

## KNOWN BUGS AND INCOMPLETE PARTS:
- What parts of the project you were not able to complete

## REFERENCES:
- List any outside resources used

## MISCELLANEOUS COMMENTS:
- Anything you would like the grader to know

## Assignment Description
***
# Project 2 - Ants
### Due Date: 11:59 p.m., October 26th, 2018

*All programs will be tested on the machines in the Q22 lab. If your code does not run on the system in this lab, it is considered non-functioning EVEN IF IT RUNS ON YOUR PERSONAL COMPUTER. Always check that your code runs on the lab machines before submitting.*

### Driver Code and Test Files
* project2.py

### Grading Rubric
**Total: 60 points**
* Meadow (12 points)
    * Meadow class with a fixed sized grid (3 points)
    * Each grid cell contains hill, food, and ant references (2 pts)
    * Anthills are spawned during initialization using Builder pattern (3 points)
    * The simulation ends when only 1 or less anthills remains (2 points)
    * Each cycle is managed by the meadow (2 pts)
* Anthills (13 Points)
    * Anthills contains references to all Ants and Rooms (2 points)
    * Anthill creates ants each cycle using its rooms (3 points)
    * Each cycle, an anthill can only create a number of ants equalling the maximum number of workers, total rooms, and does not exceed the grid size (5 points)
    * All wandering ants move randomly every cycle (3 points)
* Ants (16 Points)
    * Forager finds food and returns it to the anthill (3 points)
    * Foragers have a chance to die when encountering Warriors (1 point)
    * When two warriors meet, a unique algorithm determines the outcome (2 points)
    * When a warrior happens on another Anthill, there is a small chance the Anthill will be obliterated, otherwise the warrior dies (2 points)
    * When a warrior wins a fight, it gains some attribute decorator (5 points)
    * Ants do not leave the meadow when they move (2 points)
    * Worker ants die when they create a room (1 points)
* Room (6 points)
    * Each room creates a specific type of ants each cycle if there are enough workers (3 points)
    * Creating new rooms cost 1 food and kills the worker (3 points)
* Display (13 points)
    * A menu that asks the user to display state or run for n cycles (3 points)
    * Displays when a warrior enters a fight (2 points)
    * Displays when a forager finds and returns food (2 points)
    * Display when a builder creates a room (2 points)
    * Displays when an Anthill is destroyed (2 points)
    * Display summary when only one or less anthill is left (2 points)
* Submission:
    * Follows requested project structure and submission format (-5 points)
    * No global variables (-5 points)
    * Meets the commit requirement of having 3 significant commits 24 hours apart




## Description


For our second assignment we are going to build an Ant Farm where several colonies of ants battle it out to be the last AntHill standing.

You are going to build an antfarm, and you're going to use some common design patterns to do it. The program will create several anthills in a meadow using the builder pattern. Each anthill will act as a factory that builds different kinds of Ants. What kinds of ants are built each turn will depend on the Anthill factories. Ants must leave the anthill and randomly wander the meadow in search of food.  When they do, they may randomly run into other ants. If the other ant is from another hill and is of a certain type, they should fight. The program will run cycles in which the state of the meadow will print to the console each cycle. The program will continue until only a single anthill is left.

