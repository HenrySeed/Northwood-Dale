from northwood_vale.utils import *
from northwood_vale.player import *

def menu():
    '''returns player class after either loading it or making a new one'''

    quit = False
    while quit == False:
        clear()
        print("\n" * 8)
        print("              (P)lay Game")
        print("              (L)oad Game")
        print("              (Q)uit Game")
        print("\n" * 8)

        prompt = input("*-|===> ")

        if prompt.lower() in ['q', 'quit', 'quit game']:
            quit = True

        elif prompt.lower() in ["play", "p", "play game"]:
            return new()

        elif prompt.lower() in ["load", 'l', 'load game']:
            loaded = load()
            if loaded == None:
                quit = True

    return -1


def new():
    clear()
    print("\n" * 8)
    print("          What is your name Hero?\n")
    name = input("           > ")

    clear()
    player = Player(name)
    # remove before release, only for testing #
    tester(player)
    ###########################################
    return player


def print_log():
    file = open("save_games.txt", 'r')
    log = file.readlines()
    for i in log:
        i = i.strip()
    log.reverse()

    names = []
    clear()
    print("\n" * 5)
    for item in log:
        date, time, name, filename = item.split(',')
        names.append(name)
        print("              {0:10} {1} {2}".format(date, time, name))
    
    print("\n" * 5)
    file.close()
    return names


def load():
    names = print_log()
    prompt = input('*-|===> ')
    commands = ['back', 'q', 'quit', 'close', 'cancel']

    while prompt not in names and prompt not in commands:
        names = print_log()
        print("Save not found, type 'back' to return to main menu'")
        prompt = input('*-|===> ')

    if prompt in commands:
        return None

    print("yup")


##################################################################################################################

def tester(player):
    bastard_sword = Weapon("Bastard Sword", "Its a kinda longish sword", 10)
    shield = Armour("Shield", "it blocks shit", 5)
    bannana = Item("Bananna", "Good source of potassium")
    player.inventory = [bastard_sword, shield, bannana]

    player.update()