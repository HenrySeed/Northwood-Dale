from graph import *
from player import *

import os
from time import *
import re

def clear():
    os.system('clear')

def set_locations():
    descr = "Nestled near the river this large farmhouse looms over \
the flat plains as the only point on the horizon for miles. \n\
    \n\
    To the North you can spot a lookout tower in the mountains\n\
    To the West the road dips down to the river\n\
    To the East the houses stables sit near a field for horses\n\
    To the South the road leads into the horizon, Its too hazy to see"
        
    homestead = Location("Homestead", descr)
    
    descr = "Resting on the side of these mountain range is this lookout tower.\
 It looks like it has the best view in the plains. You can see as far as the\
 desert to the south of the homestead and you can see the giant tree on \
Kuldahar to the east. Far in the west the river snakes lazily across the plains.\
 This high up you feel as though you can almost touch the heavens. You should \
probably head down before you fall. It's pretty precarious up here.\n\
    \n    To the South lies the path back to the Homestead\n\
    On all other sides the mountain is too tough to climb."
    
    tower = Location("Lookout Tower", descr)
    
    descr = "The stables sit near the homestead but there are no horses \
nearby, wonder where they all went? eh, nevermind, the owner probabley \
sold them. Nothing nefarious going on here.\n\
    To the east sits Kuldahar, resting in the shade under the mile tall tree.\n\
    Back towards the West sits the Homestead."
    
    stables = Location("Homestead Stables", descr)
    
    #---------------  Sets all the Connections Now ---------------------
    
    homestead.north = tower
    tower.south = homestead
    homestead.east = stables
    stables.west = homestead
    
    return homestead


def menu():

    quit = False
    while quit == False:
        clear()
        print("\n" * 8)
        print("              (P)lay Game")
        print("              (Q)uit Game")
        print("\n" * 8)

        prompt = input("*-|===> ")

        if prompt.lower() in ['q', 'quit']:
            quit = True

        elif prompt.lower() in ["play", "p", "play game"]:
            clear()
            print("\n" * 8)
            print("          What is your name Hero?\n")
            name = input("           > ")

            clear()
            player = Player(name)
            return player
    
def main():
    current_location = set_locations()
    
    quit = False
    player = menu()
    
    if player == None:
        print("Quitting Now...")
        sleep(0.2)
        clear()
        return 0


    print(current_location)

    while quit == False:
        prompt = input("\n> ")

        if prompt in ['n', 's', 'e', 'w', 'north', 'south', 'east', 'west']:
            current_location = current_location.move(prompt)

        elif 'look' in prompt:
            current_location.look() 

        elif 'search' in prompt:
            current_location.search()

        elif prompt in ['quit', 'q']:
            print("Quitting Now...")
            quit = True
            sleep(0.2)
            clear()
    
    
    
main()


