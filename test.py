import re

def mymatch(string, pattern):
    pattern = re.compile(pattern)
    if pattern.match(string) != None:
        return True
    else:
        return False

def main():

    quit = False

    while quit == False:
        prompt = input("> ")

        if mymatch(prompt, '(/S|^/S)*([n,s,e,w]|[north,east,south,west](/S|^/S)*)'):
            print('Moved')
        elif mymatch(prompt, 'quit|q'):
            print("quitting...")
            quit = True


main()