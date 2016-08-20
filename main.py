from graph import *
from player import *
from utils import *

from time import *
import re

class Console():
    def __init__(self):
        self.set_locations()
        clear()
        quit = False
        player = Player("Hrothgar")
        bastard_sword = Item("Bastard Sword", "Its a kinda longish sword", "Weapon", 10)
        sheild = Item("Sheild", "it blocks shit", "Armour", 0, 5)
        bannana = Item("Bananna", "Good source of potassium")

        

        player.inventory = [bastard_sword, sheild, bannana]
        buffer = None

        if player == None:
            print("Quitting Now...")
            sleep(0.2)
            clear()
            return 0


        current_location = self.homestead

        print(current_location)

        while quit == False:
            prompt = input("\n> ")

            if prompt in ['n', 's', 'e', 'w', 'north', 'south', 'east', 'west']:
                current_location = current_location.move(prompt)

            elif 'look' in prompt:
                current_location.look() 

            elif 'search' in prompt:
                buffer = current_location.search()

            elif "pick" in prompt or "grab" in prompt:
                print("\nYou pick up the " + buffer.name + " and put it in your backpack.")
                player.inventory.append(buffer)
                buffer = 0
            elif 'backpack' in prompt or 'inventory' in prompt or "i" == prompt:
                player.backpack()

            elif "tell me about" in prompt or "info" in prompt or "what" in prompt:
                for i in player.inventory:
                    if i.name.lower() in prompt.lower():
                        print(i.descr)

            elif prompt in ['quit', 'q']:
                print("Quitting Now...")
                quit = True
                sleep(0.2)
                clear()

    def set_locations(self):
        descr = "Nestled near the river this large farmhouse looms over \
the flat plains as the only point on the horizon for miles. \n\
        \n\
    To the North you can spot a lookout tower in the mountains\n\
    To the West the road dips down to the river\n\
    To the East the houses stables sit near a field for horses\n\
    To the South the road leads into the horizon, Its too hazy to see"
            
        self.homestead = Location("Homestead", descr)
        l_chestplate = Item('Leather Chestplate', "Old and worn this chestplate has seen better days", "Armour", 0, 10)
        self.homestead.items.append(l_chestplate)
        
        descr = "Resting on the side of these mountain range is this lookout tower. \
It looks like it has the best view in the plains. You can see as far as the \
desert to the south of the homestead and you can see the giant tree on \
Kuldahar to the east. Far in the west the river snakes lazily across the plains.\
This high up you feel as though you can almost touch the heavens. You should \
probably head down before you fall. It's pretty precarious up here.\n\
     \n    To the South lies the path back to the Homestead\n\
     On all other sides the mountain is too tough to climb."
        
        self.tower = Location("Lookout Tower", descr)
        
        descr = "The stables sit near the homestead but there are no horses \
nearby, wonder where they all went? eh, nevermind, the owner probabley \
sold them. Nothing nefarious going on here.\n\
    To the east sits Kuldahar, resting in the shade under the mile tall tree.\n\
    Back towards the West sits the Homestead."
        
        self.stables = Location("Homestead Stables", descr)
        
        #---------------  Sets all the Connections Now ---------------------
        
        self.homestead.north = self.tower
        self.tower.south = self.homestead
        self.homestead.east = self.stables
        self.stables.west = self.homestead
        
    

    
    
console = Console()


