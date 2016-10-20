

def get_icon(string):
    icons = {'dagger': '-|==-',
            'short sword':  '-{====-',
            'bastard sword': '->=====-',
            'rapier': '-)-----',
            'long sword': '-{======-',
            'bow': '\__--__/',
            'arrow': '>---->',
            'hammer': '----1',
            'trident': '------E',
            'belt': '---U---',
            'spear': '------<>',
            'revolver': '/=--',
            'shotgun': './=====<',
            'fish on a stick': '-->^>>--',
            'chopper': '-|_____/',
            'staff': '-----==--',
            'cowbell': 'A\'',
            'femur': '()=====()',
            'shovel': '------|)',
            'axe': '-----7'
    }

    if string in icons.keys():
        return icons[string]
    else:
        return '*****'
