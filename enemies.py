from random import *

class Enemy():
    def __init__(self, level=randint(1,100)):
        self.name = self.gen_name()
        self.level = level
        self.exp = 0/100
        self.health = randint(10,20)
        self.race = self.race()
        

    
    def __str__(self):
        return self.name + '\n' + \
               str(self.level) + '\n' + \
               str(self.health) + '\n' + \
               str(self.race)

    
    def race(self):
        races = ['ork', 'spider', 'troll', 'goblin', 'thrasher', 'raider',\
                 'bandit', 'ogre', 'knight', 'eagle', 'dragon']
        
        return races[randint(0, len(races) - 1)]
        
        
    def gen_name(self):
        first = ['Boris', 'Jeff', 'Ragnak', 'Thrask','Kelvik', 'Hothyak']
        last = ['face eater', 'fire mongerer', 'the killer', 'the fighter',\
                    'the engineer', 'the gladiator']
        name = first[randint(0,len(first)-1)] + ' ' + last[randint(0,len(last)-1)] 
        return name    
        


def generate():
    hidname = ['Boris', 'Jeff', 'Ragnak', 'Thrask','Kelvik', 'Hothyak']
    hidname2 = ['face eater', 'fire mongerer', 'the killer', 'the fighter',\
                'the engineer', 'the gladiator']
    hid = hidname[randint(0,len(hidname)-1)] + ' ' + hidname2[randint(0,len(hidname2)-1)] 
    return hid

#print()
#for i in range(0,10):
    #print(generate())
