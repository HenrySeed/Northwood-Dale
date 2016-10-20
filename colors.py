class bcolors:
    purple = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    cyan = '\033[36m'

    norm = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def purple(string):
    return bcolors.purple + string + bcolors.norm

def blue(string):
    return bcolors.blue + string + bcolors.norm

def green(string):
    return bcolors.green + string + bcolors.norm

def yellow(string):
    return bcolors.yellow + string + bcolors.norm

def red(string):
    return bcolors.red + string + bcolors.norm

def cyan(string):
    return bcolors.cyan + string + bcolors.norm


def bold(string):
    return bcolors.BOLD + string + bcolors.norm