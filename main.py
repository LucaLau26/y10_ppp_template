print("WELCOME TO PALE LUNA")
print()
print("Before you play, commands go like this: 'gonorth' and 'pickup(item)' ")
print()
start = input("Ready to play? (playgame/dontplaygame) ")

inventory = []

if start == "dontplaygame":
    gamestart = False
    secondscene = False
    finalscene = False

if start == "playgame":
    print()
    print("You are in a dark room. Moonlight shines through the window.")
    print()
    print("There is a shovel, a rope, and some gold in the corner.")
    print()
    print("There is an opened door to the east.")
    print()
    userinput = input("Command? ")

    gamestart = True
    while gamestart:
        if userinput == "pickupshovel":
            inventory.append("shovel")
            print()
            print("You now have a shovel.")
            print()
            userinput = input("Command? ")
        
        if userinput == "pickupgold":
            inventory.append("gold")
            print()
            print("You now have some gold.")
            print()
            userinput = input("Command? ")

        if userinput == "pickuprope":
            inventory.append("rope")
            print()
            print("You now have a rope.")
            print()
            userinput = input("Command? ")



        if userinput == "goeast" and "shovel" in inventory and "gold" in inventory and "rope" in inventory:
            gamestart = False
            print()
            print("Reap your reward.")
            print()
            print("PALE LUNA SMILES AT YOU.")
            print()
            print("You are in a forest. There are paths to the north, west, and east.")
            print()
            userinput = input("Command? ")


            secondscene = True
            while secondscene:
                if userinput == "goeast" or "gonorth" or "gowest":
                    print()
                    print("Command not received")
                    print()
                    userinput = input("Command? ")

                if userinput == "gosouth":
                    print()
                    print("You can't go back now.")
                    print()
                    userinput = input("Command? ")

                if userinput == "usegold":
                    print()
                    print("Not here.")
                    print()
                    userinput = input("Command? ")

                if userinput == "useshovel":
                    print()
                    print("Not now.")
                    print()
                    userinput = input("Command? ")

                if userinput == "userope":
                    print()
                    print("You've already used this...")
                    print()
                    userinput = input("Command? ")

                if userinput == "PALELUNALIESHERE":
                    secondscene = False
                    print()
                    print("pale luna smiles wide.")
                    print()
                    print("There are no paths.")
                    print()
                    print("PALE LUNA SMILES WIDE.")
                    print()
                    print("The ground is soft.")
                    print()
                    print("\033[31mPALE LUNA SMILES WIDE.\033[0m")
                    print()
                    print("Here.")
                    print()
                    userinput = input("Command? ")

                    finalscene = True
                    while finalscene:
                        if userinput == "fillhole, dropgold, fillhole":
                            print()
                            print("Congratulations!!")
                            print()
                            print("—— 40.24248 ——")
                            print("—— -121.4434 ——")
                            finalscene = False
                            break

        else:
            print()
            print("Command not received.")
            print()
            userinput = input("Command? ")