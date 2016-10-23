import sys
import os
from random import randint
from locations import *
from time import sleep

def problem():
    stmnts = ['I dont understand that', 'what?', 'sorry can you rephrase that?']
    return stmnts[randint(0, len(stmnts)-1)]

def clear():
    os.system("clear && printf '\e[3j'")


def string_to_log(string, log):

    if len(string) > 66:
        string = string.split(' ')

        line = ''
        for i in string:
            if len(line + i) > 66:
                log.append(line)
                line = ''
            else:
                line += i
                line += ' '
    else:
        log.append(string)
        
def died(player):
    sleep(1)
    player.log.append('')
    player.log.append("        You died")
    player.log.append('')
    player.log.append('')
    clear()

def pwd():
    direc = os.path.dirname(os.path.realpath(__file__))
    direc.replace(' ', '\ ')
    return direc


def item_info(player, prompt):
    prompt = prompt.lower()
    prompt = prompt.split(' ')

    if 'the' in prompt:
        prompt.remove('the')
    if 'my' in prompt:
        prompt.remove('my')
    if prompt[0] == 'tell':
        item_name = prompt[3:]
    else:
        item_name = prompt[1:]
    
    item_name = ' '.join(item_name)
    
    for i in player.inventory:
        if item_name.lower() == i.name.lower():
            player.it = i
            name, descr = i.descr_printr()

            if descr == None:
                descr = ''

            player.log.append(name)
            player.log.append(descr)

            # player.log.append('')
            player.log.append('')
            return 0



def help(string, player):
    query = string.split()
    query.remove('help')
    if len(query) == 0:
        player.log.append('[ Help ]')
        player.log.append('Type "help <topic>" to get more info')
        player.log.append('')
        player.log.append('    Topics')
        player.log.append('     - (G)etting started')
        player.log.append('     - (M)oving')
        player.log.append('     - (C)ombat')
        player.log.append('     - (I)nventory')
        player.log.append('     - (Q)uests')
        player.log.append('     - (A)ll commands')
        player.log.append('')

    elif ' '.join(query).lower() in ['getting started', 'g']:
        player.log.append('There is no help I can give at the moment sorry')
        player.log.append('')

    elif ' '.join(query).lower() in ['moving', 'm']:
        player.log.append('[ Help: Moving ]')
        player.log.append('    To move around in Northward Dale simply type north, south')
        player.log.append('    east or west (n, s, e, w for short)')
        player.log.append('    When you come to a new location you havent visited before')
        player.log.append('    you will be told a description of that place. From then ')
        player.log.append('    onwards you will just get the name.')
        player.log.append('    You can type "look" to get that description again.')
        player.log.append('')

    elif ' '.join(query).lower() in ['combat', 'c']:
        player.log.append('There is no help I can give at the moment sorry')
        player.log.append('')

    elif ' '.join(query).lower() in ['inventory', 'i']:
        player.log.append('[ Help: Inventory ]')
        player.log.append('    Your inventory is where any items you are carrying will be')
        player.log.append('    held. Type "info <item>" or "tell me about <item>" to get ')
        player.log.append('    information about an item.')
        player.log.append('    The colours define rarity. The order from least to most rare:')
        player.log.append('    None > Green > Blue > Purple')
        player.log.append('    When you search at a location you can pick up any itmes with')
        player.log.append('    "pick up <item>" / "take <item>" / "take it" / "pick it up".')
        player.log.append('')

    elif ' '.join(query).lower() in ['quests', 'q']:
        player.log.append('There is no help I can give at the moment sorry')
        player.log.append('')

    elif ' '.join(query).lower() in ['all commands', 'a']:
        player.log.append('[ Help: All Commands ]')
        player.log.append('    Info / Tell me about <item>')
        player.log.append('    Take / Pick up <item>')
        player.log.append('    Moving (n,s,e,w)')
        player.log.append('    Eat <Item>')
        player.log.append('    Inventory')
        player.log.append('    Character')
        player.log.append('    Map')
        player.log.append('    Quests')
        player.log.append('    Help')
        player.log.append('')

    else:
        player.log.append('No help article on that topic exists sorry.')
        player.log.append('')
