def start():
    name = str(input("\nHello! What is your name?\n"))
    name = name[:1].upper() + name[1:]
    print("\nYou standing on a dark road in the middle of the forest. There is a sign, with directions on it. \n    North: The village of Boughstead\n    South: Boughstead manor\n")
    def north1():
        print( "you walk further up the road")
        command = input("\nWhat do you want to do " + name + "?\n>>")
        command = command.lower()
        if command == "look around":
            print("\n")
            print("There are thick trees on both sides on the road and fresh snow lying on the ground.")
        else:
            print("\n")
            print("I dont understand that")
            north1()
    def start1():
        command = input("\nWhat do you want to do " + name + "?\n>>")
        command = command.lower()
        if command == "look around" or command == "look":
            print("\n")
            print("Leaning next to the sign is a rusted bike. Apart from that there is only the endless trees. The dark feels like it's closing in")
            start1()           
        elif command == "go north" or command == "n":
            north1()     
        elif command == "ride bike":
            print("\n")
            print("You try riding it but fall over because it has no handlebars")
            start1()
        elif command == "take bike":
            print("\n")
            print("You can't take it, it has no handlebars")
            start1()
        elif command == "examine bike":
            print("\n")
            print("You examine it, it has no handlebars")
            start1()
        else:
            print("\n")
            print("I dont understand that")
            start1()
        
    start1()
start()
