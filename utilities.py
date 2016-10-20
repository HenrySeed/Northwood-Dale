import sys
import os
from random import randint
from locations import *

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
        

def pwd():
    direc = os.path.dirname(os.path.realpath(__file__))
    direc.replace(' ', '\ ')
    print(direc)
    return direc
