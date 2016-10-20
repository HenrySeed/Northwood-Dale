
def locations_importer():
    file = open(pwd() + "/locations.txt", 'r')
    lines = file.readlines()
    locations = []
    location = ["", ""]

    for line in lines:
        if line[0] == '#':
            if location != ["", ""]: locations.append(location)
            location = [line[2:].strip(), ""]
        elif line != '\n' and line != '':
            location[1] += line
    
    if location != ["", ""]: locations.append(location)

    homestead = Location(locations[0])
    tower = Location(locations[1])
    stables = Location(locations[2])

    #l_chestplate = Item('Leather Chestplate', "Old and worn this chestplate has seen better days", "Armour", 0, 10)
    #homestead.items.append(l_chestplate)
    
    #---------------  Sets all the Connections Now ---------------------
    
    homestead.north = tower
    tower.south = homestead
    homestead.east = stables
    stables.west = homestead

    return homestead
