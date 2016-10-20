class Player():
    
    '''Creates an instance of the Player'''
    
    def __init__(self, name='', level=1):
        '''Establishes variables used in player class'''
        self.name = name
        self.exp = 1670
        self.level = 1
        self.next_level = (self.level+1) * 1000
        
        self.health = 10
        self.max_health = 20
        self.strength = 10
        
        self.position = [16, 10]
        self.current_map = None
        self.current_quest = []
        
        self.inventory = []

        self.log = ['']
        
        
    def print_inventory(self):
        '''Prints self.inventory in dynamic table'''
        
        max_width = self.inv_max_width()
        bar = '+' + ('-' * 11) + '-' + ('-' * (max_width + 2)) + '+' + ('-' * 5) + '+'
        
        self.log.append(bar)
        self.log.append('|  {0:{width}} | {1:3} |'.format('item', 'DMG', width=(max_width+11)))
        self.log.append(bar)
        
        for i in self.inventory:
            name = i.__str__()
            dmg = i.dmg
                
            self.log.append('|  {0:9}  {1:{width}} | {2:<3} |'.format(i.icon, name, dmg, width=max_width))
            
        self.log.append(bar)
        self.log.append('')


        
    def north(self):
        self.position[1] = self.position[1] - 1
        
    def south(self):
        self.position[1] = self.position[1] + 1  
        
    def east(self):
        self.position[0] = self.position[0] + 1
    
    def west(self):
        self.position[0] = self.position[0] - 1

    def print_quests(self):
        print()
        print()
        
        
    def print_char_info(self):
        '''print's a table of info about your character'''
        
        self.log.append('+' + (12 * '-') + '+' + (10 * '-') + '+')
        self.log.append('|' + ' Name       | {0:<9}|'.format(self.name))
        self.log.append('+' + (12 * '-') + '+' + (10 * '-') + '+')
        self.log.append('|' + ' Level      | {0:<9}|'.format(self.level))
        self.log.append('|' + ' Health     | {0:<9}|'.format(self.health))
        self.log.append('|' + ' Strength   | {0:<9}|'.format(str(self.position)))
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
        self.log.append('+' + ('-' * 20) + '+')  
        self.log.append('') 
        
    def inv_max_width(self):
        '''finds the maximum width of the items column of the inventory'''
        
        max_width = 0
        for i in self.inventory:
            if len(i.__str__()) > max_width:
                max_width = len(i.__str__())
                
        return max_width
    
    def pane(self):
        health = self.health
        max_health = self.max_health
        health_ratio = health/max_health
        
        exp = self.exp
        nec_level = self.next_level
        exp_ratio = exp/nec_level
        
        pane_lines = []
        
        pane_lines.append('')
        pane_lines.append('  Health [{0:14}]'.format(int(health_ratio * 14) * '#'))
        pane_lines.append('             {0} / {1}'.format(health, max_health))
        pane_lines.append('')
        pane_lines.append('  EXP    [{0:14}]'.format(int(exp_ratio * 14) * '#'))
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
    
    

    
