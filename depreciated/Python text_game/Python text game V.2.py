import math
def main():
    """runs the gaim"""
    derp = str(input("\nHello! What is your name?\n>>"))
    derp = derp.capitalize()
    print("\nYou are standing on a dark road in the middle of the " + \
            "forest. There is a sign, with directions on it.")
    print("\n    North: The village of Boughstead")
    print("    South: Boughstead village")
    print("\nYou may want to search or look around for things here to " + \
          "better your travels.\n")
    def inventory():
        """reads the inventory list and prints as a formatted list."""
        dash_bar = ""
        inv = ["Hat", "Leather Jerkin", "Iron Sword", "Shield"]
        start = "| "
        end = " |"
        maxlength = 0
        for i in inv:
            if len(i) > maxlength:
                maxlength = 4 + len(i)
            dash_bar = "+" + ("-" * maxlength) + "+"
            row1 = "|{0:10}|".format(i)
            print(dash_bar)
            print(row1)
        print(dash_bar)
    def north1():
        """Function for game tile north 1. Prints description and has input"""
        print("Here the forest is even thicker, just like yo' Mum.")
        command = input("\nWhat do you want to do " + derp + "?\n>>")
        command = command.lower()
        print("\n")
        if command == "look around":
            print("There are thick trees on both sides on the road and " + \
            "fresh snow lying on the ground.")
        else:
            print("I dont understand that")
            north1()
    def start1():
        """Function for beginning position of game. Prints des and input"""
        command = input("What do you want to do " + derp + "?\n>>")
        command = command.lower()
        print("\n")
        if command.find("look") >= 0 or command.find("examine") >= 0 or + \
           command.find("search") >= 0:
            if command.find("bike") > command.find("look") or + \
               command.find("bike") > command.find("examine"):
                print("The bike is rusted and is missing its handlebars")
            elif command.find("sign") > command.find("look") or  + \
                 command.find("sign") > command.find("examine"):
                print("\n    North: The village of Boughstead")
                print("        South: Boughstead manor\n")
            else:
                print("Looking around, you see that leaning next to  " + \
                      "the sign is a rusted bike. Apart from that there " + \
                      "is only the endless trees. The dark feels like " + \
                      "it's closing in")
        elif command.find("inventory") >= 0 or command.find("inv") >= 0:
            inventory()
        elif command.find("take") >= 0 or command.find("pick up") >= 0:
            if command.find("bike") > command.find("take") or + \
               command.find("bike") > command.find("pick up"):
                print("You can't take it, it has no handlebars")
            elif command.find("sign") > command.find("take") or + \
                 command.find("sign") > command.find("pick up"):
                print("You try to rip the street sign out of the " + \
                "ground but it is stubbornly staying put.")
            else:
                print("I dont understand that")
        elif command.find("ride") >= 0:
            if command.find("bike") > command.find("ride"):
                print("You can't ride it, it has no handlebars")
            else:
                print("I dont understand that")
        elif command.find("go") >= 0 or command.find("walk") >= 0 or + \
             command.find("travel") >= 0:
            if command.find("north") > command.find("go") or + \
               command.find("north") > command.find("walk") or + \
               command.find("north") > command.find("travel"):
                print("You walk northwards up the road towards " + \
                      "The village of Boughstead.")
            elif command.find("go") > command.find("south") or + \
                 command.find("walk") > command.find("south") or + \
                 command.find("travel") > command.find("south"):
                print("You walk Southwards towards Boughstead manor")            
            else:
                print("I dont understand that")
            north1() 
        elif command == "ride bike":
            print("The bike has no handlebars. You try riding it but " + \
            "fall over because you can't ride a bike with no handlebars")
        elif command.find("stroke sword") >= 0:
            print("You shine your sword till its polish leaks all " + \
                  "over the floor...")
        else:
            print("I dont understand that")    
        print("\n")
        start1()
    start1()
main()