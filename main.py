print("WELCOME TO PALE LUNA")
print()
print("Before you play, commands go like this: 'go north' and 'pick up (item)' ")
print()
start = input("Ready to play? (play_game/dont_play_game) ")

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

    if userinput == "pick_up_shovel" or :
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

    elif userinput == "pick_up_gold":
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

    if userinput == "go_east" and "shovel" in inventory and "gold" in inventory:
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