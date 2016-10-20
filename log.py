def display_log(old_log):

    log = []
    log += old_log
    length = 34

    log.reverse()
    result = [''] * length
    
    for i in range(0, length):
        try:
            result[i] = log[i]
        except:
            result[i] = ''

    result.reverse()

    # print(log)
    # print(result)

    return result


def add_to_log(log, prompt):
    dictionary = {
                  "map": "Opened Map",
                  "m": "Opened Map",
                  "quests": "Opened Quests",
                  "q": "Opened Quests",
                  }
    ignore = ['e', 'east','w', 'west','n', 'north','s', 'south', '\\x1b[A', '\\x1b[C', '\\x1b[D', '\\x1b[B', 'i', 'inv', 'inventory', 'c', 'char', 'character', '?', 'help', 'h']

    if prompt.lower() in dictionary.keys():
        log += [dictionary[prompt.lower()]]
        log += ['']

    elif prompt.lower() not in ignore:
        log += [prompt]
        log += ['']