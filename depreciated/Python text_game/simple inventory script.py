import math

def inventory():
    bar = ""
    inv = ["stuff", "things", "hat", "zara"]
    items = len(inv)
    start = "| "
    middle = " | "
    end = " |"
    maxL = 0
    for i in inv:
        if len(i) > maxL:
            maxL = len(i)
            
    for i in inv:
        spaces1 = " " * math.floor((maxL - len(i) + 2)/2)
        spaces2 = " " * math.ceil((maxL - len(i) + 2)/2)
        bar = ("-" * (6 + maxL))
        row1 = start + spaces1 + i + spaces2 + end
        print(bar)
        print(row1)
    print(bar)
        