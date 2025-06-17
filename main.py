print("WELCOME TO PALE LUNA")
print()
print("Before you play, commands go like this: 'go north' and 'pick up (item)' ")
print()
start = input("Ready to play? (play game/dont play game) ")

inventory = []

if start == "dont_play_game":
    gamestart = False
    secondscene = False

elif start == "play_game":
    gamestart = True
    while gamestart:
        print()
        print("You are in a dark room. Moonlight shines through the window.")
        print()
        print("There is a shovel to the south, and some gold to the west.")
        print()
        print("There is a door to the east.")
        print()
        userinput = input("Command? ")

        if userinput == "pickupshovel":
            inventory.append("shovel")
            print()
            print("You now have a shovel.")
            print()
            userinput == input("Command? ")
            if "shovel" in inventory:
                print()
                print("You already have that.")
                print()
                userinput = input("Command? ")
        
        elif userinput == "pickupgold":
            inventory.append("gold")
            print()
            print("You now have some gold.")
            print()
            userinput = input("Command? ")
            if "shovel" in inventory and "gold" in inventory:
                print()
                print("You now have both a shovel and some gold.")
                print()
                userinput = input("Command? ")
            if "gold" in inventory:
                print()
                print("You already have that.")
                print()
                userinput = input("Command? ")

        else:
            print()
            print("Command not received.")
            print()
            userinput = input("Command? ")    

        if userinput == "go east" and "shovel" in inventory and "gold" in inventory:
            secondscene = True
        else:
            print()
            print("You can't do that yet.")
            print()
            userinput = input("Command? ")
            
    gamestart = False

    while secondscene:
        print()
        print("PALE LUNA SMILES AT YOU.")
        print()
        print("You are in a forest. There are paths to the north, west, and east.")
        print()
        userinput = input("Command? ")

        if userinput == "go east" or "go north" or "go west":
            print()
            print("Command not received")
            print()
            userinput = input("Command? ")

        elif userinput == "go south":
            print()
            print("You can't go back now.")
            print()
            userinput = input("Command? ")

        elif userinput == "PALELUNALIESHERE":
            finalscene = True

        else:
            print()
            print("Command not received.")
            print()
            userinput = input("Command? ")

while finalscene:
    print()
    print("pale luna smiles wide.")
    print()
    print("There are no paths.")
    print()
    print("PALE LUNA SMILES WIDE.")
    print()
    print("The ground is soft.")
    print()
    print("\033[31mPALE LUNA SMILES WIDE.\033[31m")
    print()
    print("Here.")
    print()
    userinput = input("Command? ")