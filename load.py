import re

def load_file(filename):
    try:
        input_file = open(filename, 'r')
        lines = input_file.readlines()
        input_file.close()
        for i in range(0, len(lines)):
            lines[i] = lines[i][:-1]
        return lines
    
    except FileNotFoundError:
        return "A file could not be found."
        
        


        
    
            
    