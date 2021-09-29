#A cat's room escape

import sys

player = {
    "name":"p1",
    "dried fish": 0,
    "items": [],
    "location":"start"
}

driedFish = {
    "desk": 1,
    "sofa": 1,
    "cat tree": 1,
    "tv": 1,
    "box": 1,
    "pillow": 1,
    "painting": 1,
    "closet": 1
}

def printGraphic(name):
    if (name == "cat"):
        print(" _._     _,-'""`-._"     )
        print("(,-.`._,'(       |\`-/| ")
        print("    `-.-' \ )-`( , o o) ")
        print("          `-    \`_`'''-")

    if (name == "fish"):
        print("You get a dried fish!")
        print("         _           ")
        print("       ><_>          ")

    if (name == "gameover"):
        print("  ,-.       _,---._ __  / \   ")
        print(" /  )    .-'       `./ /   \  ")
        print("(  (   ,'            `/    /| ")
        print(" \  `-'             \'\   / | ")
        print("  `.              ,  \ \ /  | ")
        print("   /`.          ,'-`----Y   | ")
        print("  (            ;        |   ' ")
        print("  |  ,-.    ,-'         |  /  ")
        print("  |  | (   |  game over | /   ")
        print("  )  |  \  `.___________|/    ")
        print("  `--'   `--'                 ")

    if (name == "success"):
        print("    ▒▒▒▒  ▒▒▒▒                          ")                     
        print("  ▒▒  ▒▒▒▒▒▒▒▒▒▒                        ")
        print("  ▒▒▒▒  ▒▒▒▒▒▒▒▒                        ")
        print("    ▒▒▒▒▒▒▒▒▒▒                          ")
        print("      ▒▒▒▒▒▒                            ")
        print("        ▒▒                              ")
        print("    ██          ██                      ")
        print(" ██░░██      ██░░██                     ")
        print(" ██░░░░██████░░░░██                     ")
        print("██░░░░░░░░░░░░░░░░░░██                  ")
        print("██░░░░░░░░░░░░░░░░░░██                  ")
        print("██░░██░░░░░░░░██░░░░██                  ")
        print("██░░██░░░░░░░░██░░░░██    ████          ")
        print("██░░░░░░░░░░░░░░░░░░██  ██    ██        ")
        print("████▒▒▒▒▒▒▒▒▒▒████    ██    ██          ")
        print("    ██░░▒▒▒▒░░░░░░██    ██    ██        ")
        print("    ██░░██░░████░░░░██  ██░░░░██        ")
        print("    ██░░████░░░░██░░██  ██░░░░██        ")
        print("    ██  ████░░░░░░░░████▒▒▒▒▒▒██        ")
        print("    ██  ██    ░░░░░░██▒▒▒▒████          ")
        print("    ██████████████████████              ")
        print                                        
        print("████  ████  ██████    ████    ██      ██")
        print("██  ██  ██  ██      ██    ██  ██      ██")
        print("██      ██  ████    ██    ██  ██      ██")
        print("██      ██  ██      ██    ██  ██  ██  ██")
        print("██      ██  ██████    ████      ██  ██  ")
    
    if (name == "satisfiedCat"):
        print("                ████████████████                              ")
        print("            ████░░░░░░░░░░░░░░░░████                          ")
        print("██████████████░░░░░░░░░░░░░░░░░░░░░░░░████████████            ")
        print("██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██            ")
        print("██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██            ")
        print("██▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓██                ")
        print("██▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓██                ")
        print("    ██▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓██                ")
        print("    ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██                    ")
        print("    ██░░░░░░████░░░░░░░░░░░░░░████░░░░░░██                    ")
        print("    ██░░░░██  ▒▒██░░░░░░░░░░██  ▒▒██░░░░██                    ")
        print("    ██░░░░██▒▒▒▒██░░░░░░░░░░██▒▒▒▒██░░░░██                    ")
        print("        ██░░░░████░░░░░░░░░░░░░░████░░░░██                    ")
        print("        ██░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░██                    ")
        print("    ▓▓▓▓▓▓██░░░░▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓░░░░██                      ")
        print("▓▓▒▒▒▒▒▒▓▓██▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██                          ")
        print("▓▓▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓▒▒▓▓██                        ")
        print("    ▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓██                    ")
        print("▓▓▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓▒▒▓▓░░░░██        ██████      ")
        print("▓▓▒▒▒▒▒▒▓▓  ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓░░░░░░██        ██▓▓▓▓██    ")
        print("    ▓▓▓▓▓▓    ██▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓░░░░░░░░░░██        ██▓▓▓▓██")
        print("            ██░░░░▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░██        ██▓▓▓▓██  ")
        print("                ██░░░░░░░░░░░░░░██░░░░░░░░░░██        ██░░▓▓██")
        print("                ██░░░░░░██░░░░░░██░░░░░░░░░░██      ██░░░░░░██")
        print("                ██░░░░░░██░░░░░░██░░░░░░░░░░██      ██░░░░██  ")
        print("                ██░░░░░░██░░░░░░██░░░░░░░░░░██    ██░░░░░░██  ")
        print("                ██░░░░██░░░░██░░░░░░░░░░░░██████░░░░░░██      ")
        print("                ██░░░░██░░░░██░░░░░░░░░░░░░░░░░░░░████        ")
        print("                ██░░░░██░░░░██░░░░░░░░░░░░████████            ")
        print("                    ████  ██████████████████                  ")

    if (name == "stars"):
        print("      ,          ")
        print("   \  :  /       ")
        print("`. __/ \__ .'    ")
        print("_ _\     /_ _    ")
        print("   /_   _\       ")
        print(" .'  \ /  `.     ")
        print("   /  :  \       ")
        print("      '          ")


def introStory():
    print("Hi! What should I call you?")
    player["name"] = raw_input("Please enter your name: ")
    print
    print("Welcome to the A cat's room escape " + player["name"] + "!")
    print
    print("Several days ago, when you woke up, you found a human being was sleeping on the bed. ")
    print("And you... You became a cat! ")
    print("It took you a while to figure out what the hell was going on. ")
    print("It seemed like you have swapped the body with a cat. But obviously the cat's owner didn't realize that. ")
    print("Today, when your owner is still asleep, you think you can not just wait any longer. ")
    print("You want to go out to find some clues. So you must open the door before the owner wake up. ")
    print
    print("Now you can walk around the room and find a way to escape. ")

def gameOver():
    print("You have failed to escape the room.")
    print
    printGraphic("gameover")
    print
    print("------------------------------------------")
    print("Your name: " + player["name"])
    print("You have " + str(player["dried fish"]) + " dried fish.")
    print("To be continued...")
    sys.exit()

def desk():
    if (driedFish["desk"] >= 1):
        player["dried fish"] = int(player["dried fish"]) + 1
        printGraphic("fish")
        print("You have " + str(player["dried fish"]) + " dried fish now.")
        driedFish["desk"] = driedFish["desk"] - 1
        print
        driedFishList()

    if ("pen" in player["items"]):
        print("You find a cup on the desk")
        print("Do you want to pick up the cup?")
        print("[options: yes, no]")
        cupChoice = raw_input(">")
        if (cupChoice == "yes"):
            print
            print("Unfortunately, you break the cup and wake up the owner.")
            gameOver()
        else:
            print("Back to the front of the room.")
            print
            front()
    else:
        print("You find a pen and a cup on the desk.")
        print("Do you want to pick up anything?")
        print("[options: pen, cup, nothing]")
        deskChoice = raw_input(">")
        if (deskChoice == "pen"):
            player["items"].append("pen")
            print
            print("You get a pen!")
            print
            desk()
        elif (deskChoice == "cup"):
            print
            print("Unfortunately, you break the cup and wake up the owner.")
            gameOver()
        else:
            print("Back to the front of the room.")
            print
            front()

def sofa():
    if (driedFish["sofa"] >= 1):
        player["dried fish"] = int(player["dried fish"]) + 1
        printGraphic("fish")
        print("You have " + str(player["dried fish"]) + " dried fish now.")
        driedFish["sofa"] = driedFish["sofa"] - 1
        print
        driedFishList()
        front()
    else:
        print("There is nothing on the sofa. ")
        print("Back to the front of the room.")
        print
        front()

def balcony():
    print("Which thing do you want to check?")
    print("[options: window, litter box, cat tree, go back]")
    balconyChoice = raw_input(">")
    print
    if (balconyChoice == "window"):
        print("You fall down from the window.")
        gameOver()
    elif (balconyChoice == "litter box"):
        print("There is nothing in the litter box.")
        print("Back to the balcony")
        print
        balcony()
    elif (balconyChoice == "cat tree"):
        if (driedFish["cat tree"] >= 1):
            player["dried fish"] = int(player["dried fish"]) + 1
            printGraphic("fish")
            print("You have " + str(player["dried fish"]) + " dried fish now.")
            driedFish["cat tree"] = driedFish["cat tree"] - 1
            print
            driedFishList()

        if ("hook" in player["items"]):
            print("There is nothing on the cat tree.")
            print("Back to the balcony")
            print
            balcony()
        else:
            print("You find a hook.")
            print("Do you want to pick up the hook?")
            print("[options: yes, no]")
            hookChoice = raw_input(">")
            if (hookChoice == "yes"):
                player["items"].append("hook")
                print
                print("You get a hook!")
                print("Back to the balcony")
                print
                balcony()
            else:
                print("Back to the balcony")
                print
                balcony()
    else:
        print("Back to the front of the room.")
        print
        front()

def tv():
    if (driedFish["tv"] >= 1):
        player["dried fish"] = int(player["dried fish"]) + 1
        printGraphic("fish")
        print("You have " + str(player["dried fish"]) + " dried fish now.")
        driedFish["tv"] = driedFish["tv"] - 1
        print
        driedFishList()
        left()
    else:
        print("There is nothing near the TV. ")
        print("Back to the left of the room.")
        print
        left()

def tvStand():
    if ("wires" in player["items"]):
        print("There is nothing on the TV stand.")
        print("Back to the left of the room.")
        print
        left()
    else:
        print("You find some wires.")
        print("Do you want to pick up them?")
        print("[options: yes, no]")
        wiresChoice = raw_input(">")
        if (wiresChoice == "yes"):
            player["items"].append("wires")
            print
            print("You get some wires!")
            print("Back to the left of the room.")
            print
            left()
        else:
            print("Back to the left of the room.")
            print
            left()

def shelf():
    print("Which thing do you want to check?")
    print("[options: box, catnip, go back]")
    shelfChoice = raw_input(">")
    print
    if (shelfChoice == "catnip"):
        print("You are addicted to the catnip.")
        gameOver()
    elif (shelfChoice == "box"):
        if (driedFish["box"] >= 1):
            player["dried fish"] = int(player["dried fish"]) + 1
            printGraphic("fish")
            print("You have " + str(player["dried fish"]) + " dried fish now.")
            driedFish["box"] = driedFish["box"] - 1
            print
            driedFishList()
            shelf()
        else:
            print("There is nothing in the box.")
            print("Back to the shelf")
            print
            shelf()
    else:
        print("Back to the left of the room.")
        print
        left()

def pillow():
    if (driedFish["pillow"] >= 1):
        player["dried fish"] = int(player["dried fish"]) + 1
        printGraphic("fish")
        print("You have " + str(player["dried fish"]) + " dried fish now.")
        driedFish["pillow"] = driedFish["pillow"] - 1
        print
        driedFishList()
        right()
    else:
        print("There is nothing under the pillow. ")
        print("Back to the right of the room.")
        print
        right()

def potPlant():
    print("You eat the plant and get poisoned.")
    gameOver()

def painting():
    print("Do you want to check the back of the painting?")
    print("[options: yes, no]")
    paintingChoice = raw_input(">")
    print
    if (paintingChoice == "yes"):
        if (driedFish["painting"] >= 1):
            player["dried fish"] = int(player["dried fish"]) + 1
            printGraphic("fish")
            print("You have " + str(player["dried fish"]) + " dried fish now.")
            driedFish["painting"] = driedFish["painting"] - 1
            print
            driedFishList()
            right()
        else:
            print("There is behind the painting. ")
            print("Back to the right of the room.")
            print
            right()
    else:
        print("Back to the right of the room.")
        print 
        right()
    
def bed():
    print("You find the owner sleeping on the bed.")
    print("Do you want to go ahead? ")
    print("[options: yes, no]")
    bedChoice == raw_input(">")
    print
    if (bedChoice == "yes"):
        print("You directly jump on the owner and wake up her.")
        gameOver()
    elif (bedChoice == "no"):
        print("Back to the back of the room.")
        print
        back()

def closet():
    if (driedFish["closet"] >= 1):
        player["dried fish"] = int(player["dried fish"]) + 1
        printGraphic("fish")
        print("You have " + str(player["dried fish"]) + " dried fish now.")
        driedFish["closet"] = driedFish["closet"] - 1
        print
        driedFishList()

    if (("hanger" in player["items"]) and ("step stool" in player["items"])):
        print("There is nothing in the closet.")
        print("Back to the back of the room.")
        print
        back()
    elif (not("hanger" in player["items"]) and ("step stool" in player["items"])):
        print("You find some hangers in the closet. ")
        print("Do you want to pick up one?")
        print("[options: yes, no]")
        hangerChoice = raw_input(">")
        if (hangerChoice == "yes"):
            player["items"].append("hanger")
            print
            print("You get a hanger!")
            print
            closet()
        else:
            print("Back to the back of the room.")
            print
            closet()
    elif (("hanger" in player["items"]) and not("step stool" in player["items"])):
        print("You find a step stool in the closet. ")
        print("Do you want to pick up this?")
        print("[options: yes, no]")
        stoolChoice = raw_input(">")
        if (stoolChoice == "yes"):
            player["items"].append("step stool")
            print
            print("You get a step stool!")
            print
            closet()
        else:
            print("Back to the back of the room.")
            print
            closet()
    else:
        print("You find some hangers and a step stool in the closet.")
        print("Do you want to pick up anything?")
        print("[options: hanger, step stool, nothing]")
        closetChoice = raw_input(">")
        if (closetChoice == "hanger"):
            player["items"].append("hanger")
            print
            print("You get a hanger!")
            print
            closet()
        elif (closetChoice == "step stool"):
            player["items"].append("step stool")
            print
            print("You get a step stool!")
            print
            closet()
        else:
            print("Back to the back of the room.")
            print
            back()

def door():
    print("Now you are in front of the only door in this room.")
    print("Do you want to try to escape?")
    print("[options: yes, no]")
    doorChoice = raw_input(">")
    print
    if (doorChoice == "yes"):
        if (("hanger" in player["items"]) and ("step stool" in player["items"])):
            printGraphic("success")
            print
            print("You succeed!!!")
            print("You jump up from the step stool and use the hook to open the door!")
            print("Congradulations~")
            print
            print("------------------------------------------")
            print("Your name: " + player["name"])
            print("You have " + str(player["dried fish"]) + " dried fish.")
            print("To be continued...")
        else:
            print("It seems that you don't have enough tools to open the door.")
            print("Try to find more things.")
            print
            print("Back to the back of the room.")
            print
            back()
    else:
        print("Back to the back of the room.")
        print
        back()


def front():
    print("There are three areas. Which one do you want to explore? ")
    print("[options: desk, sofa, balcony, go back] ")
    frontChoice = raw_input(">")
    print
    if (frontChoice == "desk"):
        desk()
    elif (frontChoice == "sofa"):
        sofa()
    elif (frontChoice == "balcony"):
        balcony()
    else:
        chooseDirection()

def left():
    print("There are three areas. Which one do you want to explore? ")
    print("[options: tv, tv stand, shelf, go back] ")
    leftChoice = raw_input(">")
    print
    if (leftChoice == "tv"):
        tv()
    elif (leftChoice == "tv stand"):
        tvStand()
    elif (leftChoice == "shelf"):
        shelf()
    else:
        chooseDirection()

def right():
    print("There are three things. Which one do you want to check? ")
    print("[options: pillow, pot plant, painting, go back] ")
    rightChoice = raw_input(">")
    print
    if (rightChoice == "pillow"):
        pillow()
    elif (rightChoice == "pot plant"):
        potPlant()
    elif (rightChoice == "painting"):
        painting()
    else:
        chooseDirection()

def back():
    print("There are three areas. Which one do you want to explore? ")
    print("[options: bed, closet, door, go back] ")
    backChoice = raw_input(">")
    print
    if (backChoice == "bed"):
        bed()
    elif (backChoice == "closet"):
        closet()
    elif (backChoice == "door"):
        door()
    else:
        chooseDirection()


def chooseDirection():
    print("Where do you want to check? ")
    print("[options: front, left, right, back]")
    Direction = raw_input("You will go: ")
    print
    if (Direction == "front"):
        front()
    elif (Direction == "left"):
        left()
    elif (Direction == "right"):
        right()
    elif (Direction == "back"):
        back()

def driedFishList():
    if (player["dried fish"] == 8):
        printGraphic("stars")
        print("You have found all the dried fishes in this room!")
        print
        printGraphic("satisfiedCat")
        print
        print("You feel very satisfied looking at so many dried fish.")
        print("You suddenly feel that it is good to be a cat here.")
        print("------------------------------------------")
        print("Your name: " + player["name"])
        print("You have " + str(player["dried fish"]) + " dried fish.")
        print("To be continued...")
        sys.exit()

def main():
    printGraphic("cat")
    introStory()
    chooseDirection()

main()