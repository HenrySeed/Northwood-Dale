from utilities import *
from game_controller import *
import player


class Location():
    def __init__(self, deets, items=""):
        self.north = 0
        self.south = 0
        self.east = 0
        self.west = 0
        
        self.title = deets[0]
        self.descr = deets[1]
        
        self.first = True
        self.items = []

        self.it = None   # An abstract vartiable representing surrent focusses thing.
        
    def move(self, direc, player):
        
        direcs = {"n": self.north,
                  "s": self.south,
                  "e": self.east,
                  "w": self.west,
                  "north": self.north,
                  "south": self.south,
                  "east": self.east,
                  "west": self.west}
        
        if direcs[direc] in self.available():
            player.current_map = direcs[direc]
            player.log = ['']
            player.print("You walk along the path until you reach...")

            player.current_map.print_loc(player)

        else:
            print(self)
            player.print("There is an invisible wall blocking your way, damn devs.")
            return self


    def search(self, player):
        if self.items == []:
            player.print("You found nothing.")
        else:
            for i in self.items:
                player.print('You have found a ' + i.name)
                player.it = i
            return self.items[0]

        
    def available(self):
        result = []
        if self.north != 0: result.append(self.north)
        if self.south != 0: result.append(self.south)
        if self.east != 0: result.append(self.east)
        if self.west != 0: result.append(self.west)
            
        return result
    
    def set_descr(self, descr):
        self.descr = descr
        
    def look(self, player):
        for i in self.descr.split('\n'):
            player.print(i, 0)
        
    def print_loc(self, player):
        
        if self.first == True:
            self.first = False
            player.print('---- {} ----'.format(self.title))
            
            self.look(player)

        else:
            player.print('---- {} ----'.format(self.title))
        

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

    homestead.items.append(player.Armour('Leather Armour'))
    
    #---------------  Sets all the Connections Now ---------------------
    
    homestead.north = tower
    tower.south = homestead
    homestead.east = stables
    stables.west = homestead

    return homestead
