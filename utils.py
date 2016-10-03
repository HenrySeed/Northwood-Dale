import os
from northwood_dale.player import *
from northwood_dale.graph import *
import pickle
import datetime

def pwd():
    direc = os.path.dirname(os.path.realpath(__file__))
    direc.replace(' ', '\ ')
    print(direc)
    return direc

def clear():
    os.system('clear')


def printr(to_be_printed, tab_depth=1):
    '''(str to_be_printed, int tab_depth of 1 = 4 spaces)'''
    print('    ' * tab_depth + str(to_be_printed))


def locations_importer():
    file = open(pwd() + "/locations.txt", 'r')
    lines = file.readlines()
    locations = []
    location = ["", ""]

    for line in lines:
        if line[0] == '#':
            if location != ["", ""]: locations.append(location)
            location = [line[2:].strip(), ""]
        elif line != '\n' and line != '':
            location[1] += line
    
    if location != ["", ""]: locations.append(location)

    homestead = Location(locations[0])
    tower = Location(locations[1])
    stables = Location(locations[2])

    #l_chestplate = Item('Leather Chestplate', "Old and worn this chestplate has seen better days", "Armour", 0, 10)
    #homestead.items.append(l_chestplate)
    
    #---------------  Sets all the Connections Now ---------------------
    
    homestead.north = tower
    tower.south = homestead
    homestead.east = stables
    stables.west = homestead

    return homestead


def matcher(prompt):
    '''Is passed a string from the user input and returns a runs corrosponding command.'''

    return 0