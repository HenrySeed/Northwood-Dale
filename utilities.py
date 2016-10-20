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
