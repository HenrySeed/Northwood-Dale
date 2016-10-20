import load

icons_list = load.load_file('icons.txt')

icons = {}

for i in icons_list:
    i = i.split(',')
    icons[i[0]] = i[1]
    
    
print(icons)