from random import randint
from locations import *
from colors import *

####################################  Player   ######################################

class Player():
    
    '''Creates an instance of the Player'''
    
    def __init__(self, name='', level=1):
        '''Establishes variables used in player class'''
        self.name = name
        self.exp = 1670
        self.level = level
        self.next_level = (self.level+1) * 1000

        self.log = ['']

        self.health = 10
        self.max_health = 20
        self.strength = 10

        self.position = [16, 10]
        self.current_map = locations_importer()
        self.current_quest = []

        self.inventory = []
        self.gp = 0

        self.inv_size = 20

        self.str = 10
        self.chr = 10
        self.dex = 10


    def print(self, string, nl=1):
        self.log.append(string)
        if nl != 0:
            self.log.append('')

    def clear(self):
        self.log = ['']
        
    def take(self, item):
        if 'it' in item:
            i = self.it
            self.print("You pick up the " + i.name)
            self.inventory.append(i)
            self.current_map.items.remove(i)
        else:
            for i in self.current_map.items:
                if item.lower() == i.name.lower():
                    self.print("You pick up the " + i.name)
                    self.inventory.append(i)
                    self.current_map.items.remove(i)


    def eat(self, name):
        for i in self.inventory:
            if name.lower() == i.name.lower():
                if i.type == 'weapon' or i.type == 'armour' or i.type == 'item':
                    self.log.append('You shove the ' + i.name.lower() + ' down your throat and choke to death')
                    self.log.append('')
                    self.health = 0
                    return 0

                if i.type == 'food':
                    self.log.append('You eat the ' + i.name.lower() + '. It restores some health')
                    self.heal(5)
                    self.log.append('')
                    self.inventory.remove(i)
                    return 0


    def heal(self, amount):
        self.health = (amount + self.health) % self.max_health

    
    def print_inventory(self):
        '''Prints self.inventory in dynamic table'''
        num_items = 0
        num_weapons = 0
        num_armour = 0

        for i in self.inventory:
            if i.type == 'weapon':
                num_weapons += 1
            elif i.type == 'armour':
                num_armour += 1
            elif i.type == 'item':
                num_items += 1
        
        amount_full = '(' + str(len(self.inventory)) + '/' + str(self.inv_size) + ')'

        max_width = self.inv_max_width()
        bar = '+' + ('-' * (max_width + 23)) + '+'

        self.print(bar, 0)
        self.print('|  Inventory {0:{width}} {1:>7} gp   |'.format(amount_full, self.gp, width=max_width - 3), 0)
        
        self.print(bar, 0)
        if num_weapons > 0:
            for i in self.inventory:
                if i.type == 'weapon':
                        
                    icon = i.icon + ((9 - len(i.icon)) * ' ')
                    name = i.__str__() + ((max_width - i.name_len) * ' ')
                    dmg = str(i.dmg) + ((2 - len(str(i.dmg))) * ' ')
                    line = '|  ' + icon +  '  ' + name + '  DMG: ' + dmg + ' |'

                    if i.special != None or i.multi != None:
                        spacer = (77 - len(line)) * ' '
                    else:
                        spacer = ''

                    self.print(line + spacer, 0)

            self.print(bar, 0)

        if num_armour > 0:
            for i in self.inventory:
                if i.type == 'armour':
                    self.print('|  {0:{width}}  DEF: {1:<2} |'.format(i.__str__(), i.defence, width=max_width + 11), 0)
            self.print(bar, 0)
        
        if num_items > 0:
            for i in self.inventory:
                if i.type == 'item' or i.type == 'food' :
                    self.print('|  {0:{width}} |'.format(i.name, width=max_width + 20), 0)
            self.print(bar, 0)

        
        if num_armour == 0 and num_weapons == 0 and num_items == 0:
            self.print('|  {0:{width}} |'.format('Your Inventory is empty', width=(max_width+21)), 0)
           
        self.print('', 0)
        
        
    def print_char_info(self):
        '''print's a table of info about your character'''
        self.log.append('+' + (12 * '-') + '+' + (10 * '-') + '+')
        self.log.append('|' + ' Name       | {0:<9}|'.format(self.name))
        self.log.append('+' + (12 * '-') + '+' + (10 * '-') + '+')
        self.log.append('|' + ' Level      | {0:<9}|'.format(self.level))
        self.log.append('|' + ' Health     | {0:<9}|'.format(self.health))

        self.log.append('|' + ' Strength   | {0:<9}|'.format(self.str))
        self.log.append('|' + ' Charisma   | {0:<9}|'.format(self.chr))
        self.log.append('|' + ' Dexterity  | {0:<9}|'.format(self.dex))

        self.log.append('|' + ' Experience | {0:<9}|'.format(self.exp))
        self.log.append('' + '+' + (12 * '-') + '+' + (10 * '-') + '+')
        self.log.append('')
        
        
    def help(self):
        '''Prints a table of useful commands'''
        self.log.append('+' + ('-' * 20) + '+')
        self.log.append('| Available commands |')
        self.log.append('+' + ('-' * 20) + '+')
        self.log.append('| {0:<18} |'.format('(I)nventory'))
        self.log.append('| {0:<18} |'.format('(M)ap'))
        self.log.append('| {0:<18} |'.format('(Q)uests'))
        self.log.append('| {0:<18} |'.format('(C)haracter'))
        self.log.append('| {0:<18} |'.format('(H)elp'))
        self.log.append('| {0:<18} |'.format('(H)elp'))
        self.log.append('+' + ('-' * 20) + '+')  
        self.log.append('') 
        
    def inv_max_width(self):
        '''finds the maximum width of the items column of the inventory'''
        max_width = 0
        for i in self.inventory:
            if i.type == 'weapon':
                if i.name_len > max_width:
                    max_width = i.name_len
            else:
                if len(i.__str__()) > max_width:
                    max_width = len(i.__str__())
                
        return max_width
    
    def pane(self):

        health = self.health
        max_health = self.max_health
        health_ratio = health/max_health
        health_fill = red(int(health_ratio * 14) * '#')
        health_spacer = (14 - int(health_ratio * 14)) * ' '
        
        exp = self.exp
        nec_level = self.next_level
        exp_ratio = exp/nec_level
        exp_fill = green(int(exp_ratio * 14) * '#')
        exp_spacer = (14 - int(exp_ratio * 14)) * ' '
        
        pane_lines = []
        
        pane_lines.append('')
        pane_lines.append('  Health [' + health_fill + health_spacer + ']  ')
        pane_lines.append('             {0} / {1}'.format(health, max_health))

        pane_lines.append('')
        pane_lines.append('  EXP    [' + exp_fill + exp_spacer + ']  ')
        pane_lines.append('           {0} / {1}'.format(exp, nec_level))

        pane_lines.append('')
        pane_lines.append('')
        pane_lines.append('  (I)nventory')
        pane_lines.append('  (M)ap') 
        pane_lines.append('  (Q)uests')
        pane_lines.append('  (C)haracter')  
        pane_lines.append('  (H)elp') 
        pane_lines.append('')
        pane_lines.append('')
        
        return pane_lines


    def north(self):
        self.position[1] = self.position[1] - 1
        self.current_map.move('n')
        self.current_map.print_loc(self)
        
    def south(self):
        self.position[1] = self.position[1] + 1  
        
    def east(self):
        self.position[0] = self.position[0] + 1
    
    def west(self):
        self.position[0] = self.position[0] - 1

    def print_quests(self):
        print()
        print()


    def update(self):
        for item in self.inventory:
            if type(item) == Armour:
                self.defence += item.defence

###########################   Weapons, Armour and Items  ############################

class Item(object):
    def __init__(self, name, descr=None):
        self.name = name
        self.descr = descr

        self.type = 'item'

    def get_descr(self):
        descrs = {
                'stick':'Not really a weapon but certainly usefull.'
        }
        if self.name.lower() in descrs.keys():
            desc = descrs[self.name.lower()]
        else:
            desc = ''

        return desc

    def descr_printr(self):
        name = self.name
        return name, self.get_descr()

    def __str__(self):
        return self.name
    

class Food(object):
    def __init__(self, name, descr=None):
        self.name = name
        self.descr = descr

        self.type = 'food'

    def get_descr(self):
        descrs = {
                'banana':'A good source of potassium.',
                'apple':'One a day keeps doctor Nick away.'
        }
        if self.name.lower() in descrs.keys():
            desc = descrs[self.name.lower()]
        else:
            desc = ''

        return desc

    def descr_printr(self):
        name = self.name
        return name, self.get_descr()

    def __str__(self):
        return self.name


class Armour(object):
    def __init__(self, name, special=None):
        self.name = name
        self.defence = self.get_def()
        self.special = special
        self.type = 'armour'
    
    def get_def(self):
        defences = {
            'leather armour': 7,
            'platemail armour': 10,
            'chainmail armour': 8,
            'quilted armour': 5,
            'belt': 2
        }
        if self.name.lower() in defences.keys():
            defence = defences[self.name.lower()]
        else:
            defence = ''
        return defence
    
    def get_descr(self):
        descrs = {
            'leather armour': 'Soft, but solid armour. Not expensive but definately blocks a blow.',
            'platemail armour': 'A mix of metal plates and mail. Good quality and easy to move in.',
            'chainmail armour': 'Rings of metal form an almost living sheet of armour.',
            'quilted armour': 'Softer than leather armour. Usually used by gamekeepers and hunters.',
            'belt': 'A belt to hold all your things'
        }
        if self.name.lower() in descrs.keys():
            desc = descrs[self.name.lower()]
        else:
            desc = ''
        return desc
    
    def __str__(self):
        '''Prints the name of the weapon'''
        if self.special == None:
            return self.name
        else:
            return self.name + ' ' + self.special
    
    def descr_printr(self):
        name = self.__str__()

        return name, self.get_descr()


class Weapon(object):
    '''Generates random weapon with multiplier and special rare attribute'''
    
    def __init__(self, name, multi=None, special=None):
        self.name = name
        self.multi = multi
        self.special = special
        self.type = 'weapon'

        self.name_len = self.name_length()
        
        self.dmg = self.get_dmg()
        self.icon = self.get_icon(name.lower())


    def name_length(self):
        if self.multi == None:
            if self.special == None:
                return len(self.name)
            else:
                return len(self.name + ' ' + self.special)
        else:
            if self.special == None:
                return len(self.multi + ' ' + self.name)
            else:
                return len(self.multi + ' ' + self.name + ' ' + self.special)
    
    
    def get_icon(self, string):
        icons = {'dagger': '-|==-',
                'short sword':  '-{====-',
                'bastard sword': '->=====-',
                'rapier': '-)-----',
                'long sword': '-{======-',
                'bow': '\__--__/',
                'arrow': '>---->',
                'hammer': '----1',
                'trident': '------E',
                'spear': '------<>',
                'revolver': '/=--',
                'shotgun': './=====<',
                'fish on a stick': '-->^>>--',
                'Butchers knife': '-|_____/',
                'staff': '-----==--',
                'cowbell': 'A\'',
                'shovel': '|-----|)',
                'axe': '-----7'
        }

        if string in icons.keys():
            return icons[string]
        else:
            return '    '
    
    def get_dmg(self):
        damages = {
                'dagger': 3,
                'short sword': 4,
                'bastard sword': 5,
                'rapier': 4,
                'long sword': 6,
                'bow': 3,
                'arrow': 4,
                'hammer': 6,
                'trident': 4,
                'spear': 5,
                'revolver': 9,
                'shotgun': 10,
                'fish on a stick': 3,
                'Butchers knife': 6,
                'staff': 5,
                'cowbell': 5,
                'shovel': 2,
                'axe': 8
        }
        if self.name.lower() in damages.keys():
            dmg = damages[self.name.lower()]
        else:
            dmg = ''
        return dmg
    
    
    def get_descr(self):
        descrs = {'dagger': 'A short stabby dagger for pointed moments.',
                'short sword':  'An simple sword that makes you feel totally ordinary.',
                'bastard sword': "Makes you feel like your parents didnt love one another.",
                'rapier': 'A thin sword made for waving about more than stabbing.',
                'long sword': 'Stab fools from far away.',
                'bow': 'Efficiently moves arrows into your enemies.',
                'arrow': 'Pierce through the thickest sweater.',
                'hammer': 'Hit your enemies with the full force of a lump of steel.',
                'trident': 'Like a fork but longer and less pointy bits I guess.',
                'spear': 'An upgraded pointy stick.',
                'revolver': '6 shots in the chamber, You feeling lucky chump?',
                'shotgun': '2 barrels, Lock stock the fucking lot.',
                'fish on a stick': 'Well, a fish on a stick. What more do you need to know?',
                'Butchers knife': 'A butchers knife, still soaked in pigs blood',
                'staff': 'hardly mgical, just a long sick really',
                'cowbell': 'Ring it for your hearts content',
                'shovel': 'Old school but great for digging your enemies graves',
                'axe': 'Not really a warriors weapon but still a weapom non-the-less'
        }
        if self.name.lower() in descrs.keys():
            desc = descrs[self.name.lower()]
        else:
            desc = ''
        
        return desc


    def __str__(self):
        '''Prints the name of the weapon'''
        if self.multi == None:
            if self.special == None:
                return self.name
            else:
                return cyan(self.name + ' ' + self.special)
        else:
            if self.special == None:
                return green(self.multi + ' ' + self.name)
            else:
                return purple(self.multi + ' ' + self.name + ' ' + self.special)


    def descr_printr(self):
        name = self.__str__()

        return name, self.get_descr()
            
        
        
def random_weapon():
    weapons = ['Dagger', 'Bastard Sword', 'Long Sword', 'Staff', 'Rapier', \
                'Axe', 'Cowbell', 'Fish on a Stick', 'Hammer', 'Bow', 'Shovel']

    multis = ['Flaming', 'Frozen', 'Nasty', 'Nice', 'Sharp', 'Cracked', \
                'Shady', 'Rapid', 'Living', 'Blunt', 'Slow', 'Bramley\'s',\
                'Henry\'s', 'Fucked','Fishy', 'Tasty',
                ]

    specials = ['of Death', 'of Happiness', 'made for Killing', \
                'of Creepiness', 'of Pain', 'of Revenge', 'of Evil', \
                'of Love', 'made for Cooking',]      

    name = weapons[randint(0,len(weapons)-1)]
    if randint(0,10) > 8:
        multi = multis[randint(0,len(multis)-1)]
    else:
        multi = None

    if randint(0,200) > 190:
        special = str(specials[randint(0,len(specials)-1)])
    else:
        special = None

    new_weapon = Weapon(name, multi, special)
    return new_weapon


def random_armour():
    armours = ['Platemail Armour', 'Chainmail Armour', 'Quilted Armour', \
                'Leather Armour', 'Belt']

    specials = ['of Death', 'of Happiness', 'of Revenge', 'of Evil', \
                'of Love']    

    name = armours[randint(0,len(armours)-1)]
    if randint(0,200) > 195:
        special = str(specials[randint(0,len(specials)-1)])
    else:
        special = None
    
    new_armour = Armour(name, special)
    return new_armour


def random_item():
    items = ['Stick']
    name = items[randint(0,len(items)-1)]
    return Item(name)

def random_food():
    foods = ['banana', 'Apple']
    name = foods[randint(0,len(foods)-1)]
    return Food(name)
