import random   
import load
from icons import get_icon
    
class Weapon():
    '''Generates random weapon with multiplier and special rare attribute'''
    
    def __init__(self, name=None, multi=None, special=None):
        self.name = name
        self.multi = multi
        self.special = special
        
        self.dmg = random.randint(5,20) 
        #self.icon = self.icon_maker()
        self.icon = get_icon(name.lower())
    

    def icon_maker(self):
        icons_list = load.load_file('resources/icons.txt')
        
        icons = {}

        for i in icons_list:
            print(i)
            i = i.split(',')
            icons[i[0]] = i[1]
            
            
        return icons[(self.name).lower()]     
    
    def __str__(self):
        '''Prints the name of the weapon'''
        if self.multi == None:
            if self.special == None:
                return self.name
            else:
                return self.name + ' ' + self.special
        else:
            if self.special == None:
                return self.multi + ' ' + self.name
            else:
                return self.multi + ' ' + self.name + ' ' + self.special
            
        # insert colouring function for specials?
        
        # run through post-process for weapon-specific specials    

        
        
def random_weapon():
    weapons = ['Dagger', 'Bastard Sword', 'Long Sword', 'Staff', 'Rapier', \
                'Axe', 'Cowbell', 'Fish on a Stick', 'Hammer', 'Bow',\
                'Femur'
                ]

    multis = ['Flaming', 'Frozen', 'Nasty', 'Nice', 'Sharp', 'Cracked', \
                'Shady', 'Rapid', 'Living', 'Blunt', 'Slow', 'Bramley\'s',\
                'Henry\'s', 'Fucked','Fishy', 'Tasty',
                ]

    specials = ['of Death', 'of Happiness', 'made for Killing', \
                'of Creepiness', 'of Pain', 'of Revenge', 'of Evil', \
                'of Love', 'made for Cooking',]      

    name = weapons[random.randint(0,len(weapons)-1)]
        
    if random.randint(0,10) > 8:
        multi = multis[random.randint(0,len(multis)-1)]
    else:
        multi = None

     
    if random.randint(0,200) > 195:
        special = str(specials[random.randint(0,len(specials)-1)])
    else:
        special = None

    new_weapon = Weapon(name, multi, special)

    return new_weapon

