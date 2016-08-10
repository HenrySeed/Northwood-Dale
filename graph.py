class Location():
    def __init__(self, title, descr=""):
        self.north = 0
        self.south = 0
        self.east = 0
        self.west = 0
        
        self.title = title
        self.descr = descr
        
        self.first = True
        
    def move(self, direc):
        
        direcs = {"n": self.north,
                  "s": self.south,
                  "e": self.east,
                  "w": self.west,
                  "north": self.north,
                  "south": self.south,
                  "east": self.east,
                  "west": self.west}
        
        return direcs[direc]
        
    def available(self):
        result = []
        if self.north != 0: result.append(self.north)
        if self.south != 0: result.append(self.south)
        if self.east != 0: result.append(self.east)
        if self.west != 0: result.append(self.west)
            
        return result
    
    def set_descr(self, descr):
        self.descr = descr
        
    def look(self):
        print('\n' + self.descr)
        
    def __str__(self):
        
        if self.first == True:
            self.first = False
            return '\n---- {} ----\n'.format(self.title) + '\n' + self.descr
        else:
            return '\n---- {} ----'.format(self.title)
        
