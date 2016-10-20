from load import *

class Map():
    '''creates a map instance'''
    
    def __init__(self, player):
        '''sets up variables'''
        self.map_ = load_file('resources/map_0.txt')
        self.player_pos = player.position
        
    def print_map(self):
        '''prints a cut down version fo the map for the corner minimap'''
        y = self.player_pos[1]
        
        made_map = self.make_map()  

        mini_map = []
        
        middle = self.player_pos[0]
        left = middle - 13
        if left < 1:
            left = 0
        
        right = left + 27
        for i in made_map:
            mini_map.append(i[left:right])
            
        return mini_map[y-5:y+7]
                
    
    def make_map(self):
        
        y = self.player_pos[1]
        x = self.player_pos[0]
        map_0 = load_file('resources/map_0.txt')
        _map = []
        
        for row in map_0:
            _map += [list(row)]
        
        _map[y][x] = 'x'
        made_map = []
        
        for i in _map:
            row = ''
            for char in i:
                row += char
                
            made_map += [row]
            
        return made_map[0:]

