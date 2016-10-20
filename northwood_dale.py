#!/usr/local/bin/python3

import sys
import os

if sys.version_info < (3,0):
    os.system("clear && printf '\e[3j'")
    print('\n' * 5)

    print("           Northward Dale requires Python3.0 onwards.")
    print("           Download it here: https://www.python.org/downloads/")
    print('\n' * 5)


    sys.exit(1)
    

from player import *
from map import *
from load import *
import game_controller
from menu import *
from random import randint
from utilities import *


def precontroller(player):

    if player != None:

        test_player(player)

        my_map = Map(player)

        player.current_map.print_loc(player)

        status = game_controller.game_brain(player, my_map)
        clear()

        return status

    else:
        clear()


def test_player(player):
    ##     test code for character gen
    
        for i in range(1,10):
            player.inventory.append(random_weapon())
        for i in range(0, 3):
            player.inventory.append(random_armour() )
        player.inventory.append(random_item())
        player.inventory.append(random_item())
        player.inventory.append(random_food())
        player.gp += 10000

        ##   / test code for character gen


precontroller(Player('Hrothgar'))

def menu():
    '''returns player class after either loading it or making a new one'''

    quit = False
    while quit == False:
        clear()
        print("\n" * 8)
        print("                   (P)lay Game")
        print("                   (L)oad Game")
        print("                   (Q)uit Game")
        print("\n" * 8)

        prompt = input("       *-|===> ")

        if prompt.lower() in ['q', 'quit', 'quit game']:
            quit = True

        elif prompt.lower() in ["play", "p", "play game"]:
            status = precontroller(new())
            if status == -1:
                quit = True

        elif prompt.lower() in ["load", 'l', 'load game']:
            loaded = load()
            if loaded == None:
                quit = True
    clear()
    return None


def new():
    clear()
    print("\n" * 8)
    print("          What is your name Hero?\n")
    name = input("           > ")

    clear()
    player = Player(name)

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


# menu()
