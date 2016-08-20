import os
from player import *

def clear():
    os.system('clear')


def printr(to_be_printed, tab_depth=1):
    '''(str to_be_printed, int tab_depth 1 = 4 spaces)'''
    print('    ' * tab_depth + str(to_be_printed))

def menu():

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
            clear()
            print("\n" * 8)
            print("          What is your name Hero?\n")
            name = input("           > ")

            clear()
            player = Player(name)
            return player

        elif prompt.lower in ["load", 'l', 'load game']:
            log = loader()
            for name, date, data in log:
                print("              {0:10} {1}".format(name, date))
