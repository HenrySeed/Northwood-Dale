from northwood_dale.graph import *
from northwood_dale.player import *
from northwood_dale.utils import *
from northwood_dale.save_load import *
from northwood_dale.menu import *
from time import *
import re

def main():
    print(os.path.dirname(os.path.realpath(__file__)))
    current_location = locations_importer()
    clear()
    quit = False
    
    setup = menu()
    if setup == -1:
        print("Quitting Now...")
        quit = True
        sleep(0.2)
        clear()
        return 0

    player = setup


    buffer = None

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
        elif prompt == 'c' or 'character' in prompt:
            print(player)

        elif 'search' in prompt:
            buffer = current_location.search()

        elif "pick" in prompt or "grab" in prompt:
            print("\nYou pick up the " + buffer.name + " and put it in your backpack.")
            player.inventory.append(buffer)
            buffer = 0
        elif 'backpack' in prompt or 'inventory' in prompt or "i" == prompt:
            player.backpack()

        elif "tell me" in prompt or "info" in prompt or "what" in prompt:
            for i in player.inventory:
                if i.name.lower() in prompt.lower():
                    print(i.descr)

        elif 'save' in prompt or prompt == 'sa':
            save_game(player)

        elif prompt in ['quit', 'q']:
            print("Quitting Now...")
            quit = True
            sleep(0.2)
            clear()




