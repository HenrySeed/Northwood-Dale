from load import *

def update_gui(lines):
    
    for i in range(0,30):
        print()
        
    for i in lines:
        print(i)
        
        
def gui():
    
    choice = input('\n> ')
    if '1' in str(choice):
        update_gui(['                  [item 1]   item 2    item 3'])
    elif '2' in str(choice):
        update_gui(['                   item 1   [item 2]   item 3'])
    elif '3' in str(choice):
        update_gui(['                   item 1    item 2   [item 3]'])    
    elif str(choice) == 'clear':
        update_gui(['                   item 1    item 2    item 3'])
        
    gui()


update_gui(['                   item 1    item 2    item 3'])
gui()
