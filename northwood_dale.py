#!/usr/local/bin/python3

import sys

if sys.version_info < (3,0):
    print("Northward Dale requires Python3.0 onwards. Download it here: https://www.python.org/downloads/")
    sys.exit(1)
    

from player import *
from enemies import *
from encounters import *
from map import *
from load import *
import game_controller
from menu import menu
from random import randint
from utilities import *


import pprint

player = Player('Hrothgar')

# player = menu()

if player != None:

    ##     test code for character gen
  
    for i in range(1,10):
        player.inventory.append(random_weapon())
    for i in range(0, 3):
        player.inventory.append(random_armour() )
    player.inventory.append(random_item())
    player.inventory.append(random_item())
    player.gp += 10000

     ##   / test code for character gen

    my_map = Map(player)

    player.current_map.print_loc(player)

    game_controller.game_brain(player, my_map)
    clear()

else:
    clear()

