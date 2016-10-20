from player import *
from map import *
from log import *
from utilities import *


def gui(player, my_map, log):
    _map = my_map.print_map()
    log_index = 0
    clear()
    print()
    print('  +{0:70}+{1:27}+'.format(('-')*70, '---------------------------'))
    for i in range(0, 12):
        print('  |  {0:68}|{1:27}|'.format(log[log_index], _map[i]))
        log_index += 1

    print('  |  {0:68}+{1:27}+'.format(log[log_index], '---------------------------'))
    log_index += 1

    for i in range(0, 15):
        print('  |  {0:68}|{1:27}|'.format(log[log_index], player.pane()[i]))  
        log_index += 1

    for i in range(0, 6):
        print('  |  {0:68}|{1:27}|'.format(log[log_index], ' '))
        log_index += 1
    

    print('  +{0:70}+{1:27}+'.format(('-') * 70, '---------------------------'))
    print()

    


def game_brain(player, my_map):
    commands = {'north':        player.north,
                'n':            player.north,
                'south':        player.south,
                's':            player.south,
                'east':         player.east,
                'e':            player.east,
                'west':         player.west,
                'w':            player.west,
                'info':         player.print_char_info,
                'i':            player.print_inventory,
                'inv':          player.print_inventory,
                'inventory':    player.print_inventory,
                'c':            player.print_char_info,
                'char':         player.print_char_info,
                'character':    player.print_char_info,
                '?':            player.help,
                'h':            player.help,
                'help':         player.help
                }

    quit = False

    player.print_inventory()

    while quit == False:
        clear()
    
        gui(player, my_map, display_log(player.log))
        prompt = input('\n   > ')


        if prompt == 'q' or prompt == 'quit':
            quit = True
            clear()

        elif 'info' in prompt or 'tell me about' in prompt:
            item_info(player, prompt)

        elif prompt == 'clear':
            player.log = ['']

        elif prompt.lower() in commands.keys():
            add_to_log(player.log, prompt)
            commands[prompt.lower()]()

        else:
            add_to_log(player.log, prompt)

        
    
    
