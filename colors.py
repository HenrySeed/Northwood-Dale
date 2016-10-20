class bcolors:
    purple = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    norm = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def green(string):
    return bcolors.green + string + bcolors.norm

def purple(string):
    return bcolors.purple + string + bcolors.norm

def yellow(string):
    return bcolors.yellow + string + bcolors.norm

def bold(string):
    return bcolors.BOLD + string + bcolors.norm