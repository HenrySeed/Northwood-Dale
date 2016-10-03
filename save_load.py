import os
import datetime
from time import sleep

def cute_date():
    time = str(datetime.datetime.now()).split(' ')
    time = time[0].split('-')
    return '{}.{}.{}'.format(time[2], time[1], time[0])


def cute_time():
    time = str(datetime.datetime.now()).split(' ')
    time = (time[1].split('.')[0]).split(':')[:-1]
    if int(time[0]) > 12:
        return '{}:{}pm'.format(str(int(time[0]) - 12), time[1])
    else:
        return '{}:{}am'.format(str(int(time[0])), time[1])


def save_game(player):
    
    name = player.name.replace(' ', '_')
    name = '{},{},{}'.format(cute_date(), cute_time(), name)
    
    os.system('mkdir  ~/.pydnd/saves/{0}'.format(name))
    os.system('touch  ~/.pydnd/saves/{0}/player.txt'.format(name))
    sleep(1)
    #try:
    filehandler = open('~/.pydnd/saves/{0}/player.txt'.format(name), "wb")
    pickle.dump(player, filehandler)
    filehandler.close()
    print('Game saved')
    return 0
    # except:
    #     print('Could not save the game')
    #     return -1
    


def load_game(filename):

    return 0
