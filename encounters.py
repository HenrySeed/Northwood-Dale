import random
from enemies import *


def encounter(player):
    enemy = Enemy('klarry', randint(1,100))
    
    print()
    print('You encounter a level {0} wild enemy, with {1} hit points.'.format(enemy.level, enemy.health))
    
    
    attacking = False  
    
    choice = input('\nWhat do you want to do? attack or run?\n> ')
    if 'attack' in choice or 'hit' in choice:
        attacking = True
    elif 'run' in choice:
        encounter(player)
    elif 'inventory' in choice:
        self.inventory()
    elif 'help' in choice:
        self.help()
    
    while attacking == True and enemy.health > 0 and enemy.health > 0:
        attack(player, enemy)
        if enemy.health == 0:
            print('\nYou killed the enemy.')
            break
        if player.health == 0:
            print('\nyou die')  
            break        
        choice = input('\n> ')
        if 'yes' in choice:
            attacking = True
        elif 'run' in choice:
            print('You ran away')
            attacking = False
            break    


def attack(player, enemy):
        
        hit = randint(0,1)
        if hit == 0: # if you dont hit
            print('\nyou miss')
    
            print('\nenemy swings')
            damage_taken = randint(0,5)
            if damage_taken == 0:
                print('\nhe misses')
            else:
                print('\nhe hits and does {0} points of damage'.format(damage_taken))
                if player.health - damage_taken < 0:
                    player.health = 0 
                else:
                    player.health -= damage_taken
    
        else: # if you do hit
            damage_done = randint(5,10)
            if enemy.health - damage_done < 0:
                enemy.health = 0
        
            else:
                enemy.health -= damage_done
            print('\nYou hit the enemy, dealing {0} points of damage'.format(damage_done))
            
        print()
    


def commands(player, enemy):
    print(enemy.name, 'appears!!')
    print('************************') 
    cmd = input('Do you want to attack?').lower()
    if 'yes' in cmd:
        player.hurt()
        counter = randint(0,6)
        if counter <= 1:
            hurt(enemy,Player)
        else:
            hurt(Player,enemy)