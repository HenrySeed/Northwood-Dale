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
        print('+------Backpack------+')
        for i in self.inventory:
            if i.type == "Weapon":
                print('{0:10}| {1}'.format(i.name, i.attack))
            elif i.type == "Armour":
                print('{0:10}| {1}'.format(i.name, i.defence))
            elif i.type == "Items":
                print('{0:10}'.format(i.name))

    def update(self):
        for item in inventory:
            if item.type == 'defence':
                self.defence += item.defence



class Item():
    def __init__(self, name, descr, type="", attack=0, defence=0):
        self.defence = attack
        self.attack = defence

        self.min_str = 0
        self.min_dex = 0

        self.type = "Item"  # Item Weapon Armour

        self.name = name
        self.descr = descr


