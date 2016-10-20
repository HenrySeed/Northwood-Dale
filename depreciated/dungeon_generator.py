class Room():
    def __init__(self, pos=(0,0), width=0, height=0):
        self.width = width
        self.height = height
        self.pos = (0, 0)
        
        
class Map():
    def __init__(self):
        self.width = 20
        self.height = 10
        self.world = self.blank_map()
        
        
    def blank_map(self):
        return [self.width * ['#']] * self.height
    
    
    def add_room(self, room):
        top = room.pos[0]
        left = room.pos[1]
        right = left + room.width
        
        counter = 0
        for line in range(0, room.height):
            self.world[top + counter]
            counter += 1
        
    def __str__(self):
        whole_world = ''
        for line in self.world:
            for char in line:
                whole_world += char 
            whole_world += '\n'
                
        return whole_world
        
        
print()
world = Map()
room = Room((1,2), 4, 5)
print(world)

world.add_room(room)
print(world)
