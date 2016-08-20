from utils import *

class Player():
    def __init__(self, name):
        self.name = ""
        self.xp = 0
        self.health = 20
        self.defence = 0

        self.inventory = []

        self.str = 10
        self.char = 10
        self.dex = 10

    def injure(self, amount):
        self.health -= amount

    def backpack(self):
        print()
        printr('+-----Backpack----+--------+')
        for i in self.inventory:
            if i.type == "Weapon":
                printr("| {0:15} | {1:2} atk |".format(i.name, i.attack))
        printr('+-----------------+--------+')
        for i in self.inventory:
            if i.type == "Armour":
                printr("| {0:15} | {1:2} def |".format(i.name, i.defence))
        printr('+-----------------+--------+')
        for i in self.inventory:
            if i.type == "Item":
                printr("| {0:24} |".format(i.name))

        printr('+--------------------------+')

    def update(self):
        for item in inventory:
            if item.type == 'defence':
                self.defence += item.defence



class Item():
    def __init__(self, name, descr, type="Item", attack=0, defence=0):
        self.defence = attack
        self.attack = defence

        self.min_str = 0
        self.min_dex = 0

        self.type = type  # Item Weapon Armour

        self.name = name
        self.descr = descr


