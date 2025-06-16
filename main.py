print("WELCOME TO PALE LUNA")
print()
print("Before you play, commands go like this: 'go_north' and 'pick_up_(item)' ")
print()
start = input("Ready to play? (play_game/dont_play_game) ")

inventory = []

if start == "dont_play_game":
    pass

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

    if userinput == "pick_up_shovel":
        inventory.append("shovel")

    elif userinput == "pick_up_gold":
        inventory.append("gold")

    if userinput == "go_east" and "shovel" in inventory and "gold" in inventory:
        secondscene = True
    else: 
        print("You can't do that yet.")
        
gamestart = False

while secondscene:
    print()
    print("PALE LUNA SMILES AT YOU.")
    print()
    print("You are in a forest. There are paths to the north, west, and east.")
    print()
    userinput = input("Command? ")