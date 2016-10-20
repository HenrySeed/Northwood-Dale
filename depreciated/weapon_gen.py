import random

def weapon_gen():
    weapons = {
        1: ['Dagger', (random.randint(0,100)), [], ''],
        2: ['Bastard Sword', (random.randint(0,100)), [], ''],
        3: ['Long Sword', (random.randint(0,100)), [], ''],
        4: ['Staff', (random.randint(0,100)), [], ''],
        5: ['Rapier', (random.randint(0,100)), [], ''],
        6: ['Axe', (random.randint(0,100)), [], ''],
        7: ['Cowbell', (random.randint(0,100)), [], ''],
        8: ['Fish on a Stick', (random.randint(0,100)), [], ''],
        9: ['Hammer', (random.randint(0,100)), [], ''],
        10: ['Bow', (random.randint(0,100)), [],''],
        11: ['Femur', (random.randint(0,100)), [],''],

    }    
    weapon = weapons[random.randint(1,len(weapons))]
    
    multipliers = ['Flaming', 'Frozen', 'Nasty', 'Nice', 'Sharp', 'Cracked', \
                   'Shady', 'Rapid', 'Living', 'Blunt', 'Slow', 'Bramley\'s',\
                   'Henry\'s', 'Fucked','Fishy', 'Tasty',]
    
    specials = ['of Death', 'of Happiness', 'made for Killing', \
                'of Creepiness', 'of Pain', 'of Revenge', 'of Evil', \
                'of Love', 'made for Cooking',]
    
    multiplier_roll = random.randint(0,10)
    if multiplier_roll > 7:
        multiplier = multipliers[random.randint(0,len(multipliers)-1)]
        weapon[2].append(multiplier)    
        
    special_roll = random.randint(0,200)
    if special_roll > 195:
        special = specials[random.randint(0,len(specials)-1)]
        weapon[3] = str(special)
    
    
    return weapon

# insert colouring function for specials?

# run through post-process for weapon-specific specials



