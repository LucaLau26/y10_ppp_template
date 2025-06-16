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

    if userinput == "go_north":
        print("Command not received.")

    elif userinput == "go_south":
        print("There is a shovel in front of you.")

