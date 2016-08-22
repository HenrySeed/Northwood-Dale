import os
from player import *
from graph import *
import pickle

def clear():
    os.system('clear')


def printr(to_be_printed, tab_depth=1):
    '''(str to_be_printed, int tab_depth 1 = 4 spaces)'''
    print('    ' * tab_depth + str(to_be_printed))


def save_game(save_name, player):

    list = os.popen('ls saves').read()
    items = []
    for i in list.split('\n'):
        if i != '':
            items.append(i)

    if save_name in items:
        os.system('rm -r saves/' + save_name)
    
    os.system('mkdir saves/' + save_name)
    os.system('touch saves/' + save_name + '/' + save_name + '.txt')

    # try:
    filehandler = open('saves/' + save_name + '/' + save_name + '.txt', "wb")
    pickle.dump(player, filehandler)
    filehandler.close()
    print('Game saved')
    return 0
    # except:
    #     print('Could not save the game')
    #     return -1
    


def load_game(filename):

    return 0


def locations_importer():
    file = open("locations.txt", 'r')
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