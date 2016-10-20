#!/usr/local/bin/python3

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
  
    for i in range(1,10):
        weapon = random_weapon()
        (player.inventory).append(weapon)

    for i in range(0, 3):
        armour = random_armour() 
        (player.inventory).append(armour)

    test_item = random_item()
    (player.inventory).append(test_item)

    my_map = Map(player)

    player.gp += 10000

    player.current_map.print_loc(player)

    # pprint.pprint(player.log)

    game_controller.game_brain(player, my_map)
    clear()

else:
    clear()




#player.print_char_info()
#player.help()
#player.print_inventory()

#encounter(player)

# --------- add death messages