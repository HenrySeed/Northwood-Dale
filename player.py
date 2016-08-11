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

    def update(self):
        for item in inventory:
            if item.type == 'defence':
                self.defence += item.defence



class item():
    def __init__(self, name, descr, type=""):
        self.defence = 0
        self.attack = 0

        self.min_str = 0
        self.min_dex = 0

        self.type = "item"  # Item Weapon Armour

        self.name = name
        self.descr = descr


