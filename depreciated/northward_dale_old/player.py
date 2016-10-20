from northwood_dale.utils import *

class Player():
    def __init__(self, name):
        self.name = name
        self.xp = 0
        self.health = 20
        self.defence = 0

        self.inventory = []

        self.str = 10
        self.chr = 10
        self.dex = 10


    def __str__(self):
        print("    " + self.name)
        print("    XP:  {0}".format(self.xp))
        print("    HP:  {0}".format(self.health))
        print("    Def: {0}".format(self.defence))
        print("    Str: {0}".format(self.str))
        print("    Chr: {0}".format(self.chr))
        print("    Dex: {0}".format(self.dex))

        return "    Your backpack has {} items in it.".format(len(self.inventory))


    def injure(self, amount):
        self.health -= amount


    def backpack(self):
        print()
        printr('+-----Backpack----+--------+')
        for item in self.inventory:
            if type(item) == Weapon:
                printr("| {0:15} | {1:2} atk |".format(item.name, item.attack))
        printr('+-----------------+--------+')
        for item in self.inventory:
            if type(item) == Armour:
                printr("| {0:15} | {1:2} def |".format(item.name, item.defence))
        printr('+-----------------+--------+')
        for item in self.inventory:
            if type(item) == Item:
                printr("| {0:24} |".format(item.name))
        printr('+--------------------------+')


    def update(self):
        for item in self.inventory:
            if type(item) == Armour:
                self.defence += item.defence

    
class Item():
    def __init__(self, name, descr):
        self.name = name
        self.descr = descr

class Armour():
    def __init__(self, name, descr, defence=0):
        self.defence = defence
        self.min_str = 0
        self.min_dex = 0

        self.name = name
        self.descr = descr


class Weapon():
    def __init__(self, name, descr, attack=0):
        self.attack = attack
        self.min_str = 0
        self.min_dex = 0

        self.name = name
        self.descr = descr
