# https://github.com/Zfauser/Python-Game-Gr-9
import time
#import title
#getch from: https://stackoverflow.com/questions/27750536/python-input-single-character-without-enter
import sys
import random
def getch():
    import termios
    import sys, tty
    def _getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    return _getch()

def beep(interval = 0.1, frequency = 10):
    for i in range(frequency):
        print("\a",end="\r")
        time.sleep(interval)
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()
paths = "N(chestroom),E(weapons room),S(hallway),W(hospital)"
pathways = 4
triviagames = 0
gold = 0
room = 10
foundsecret = 0
keys = 0
climb = 0
roomname = "start"
health = 100
weapons = ["Iron Sword","Battle Axe","Fire Rod","Crossbow"]
cost = [10,15,20,25]
damage = [10,15,20,25]
inventory = []
option = 0
octocathealth = 100
SelectScreen = "1"

print("db   d8b   db d88888b db       .o88b.  .d88b.  .88b  d88. d88888b ")
print("88   I8I   88 88'     88      d8P  Y8 .8P  Y8. 88'YbdP`88 88'     ")
print("88   I8I   88 88ooooo 88      8P      88    88 88  88  88 88ooooo ")
print("Y8   I8I   88 88~~~~~ 88      8b      88    88 88  88  88 88~~~~~ ")
print("`8b d8'8b d8' 88.     88booo. Y8b  d8 `8b  d8' 88  88  88 88.     ")
print(" `8b8' `8d8'  Y88888P Y88888P  `Y88P'  `Y88P'  YP  YP  YP Y88888P ")
print(" ")
time.sleep(.7)
print("d888888b  .d88b.  ")
print("`~~88~~' .8P  Y8. ")
print("   88    88    88 ")
print("   88    88    88 ")
print("   88    `8b  d8' ")
print("   YP     `Y88P'  ")
time.sleep(.7)
print(" ")
print("      ___           ___           ___           ___           ___      ")
time.sleep(.1)
print("     /\__\         /\  \         /\__\         /\  \         /\__\     ")
time.sleep(.1)
print("    /::|  |       /::\  \       /:/  /         \:\  \       /:/ _/_    ")
time.sleep(.1)
print("   /:/:|  |      /:/\:\  \     /:/  /           \:\  \     /:/ /\  \   ")
time.sleep(.1)
print("  /:/|:|  |__   /:/ /::\  \   /:/  /  ___   ___ /::\  \   /:/ /::\  \  ")
time.sleep(.1)
print(" /:/ |:| /\__\ /:/_/:/\:\__\ /:/__/  /\__\ /\  /:/\:\__\ /:/_/:/\:\__\ ")
time.sleep(.1)
print(" \/__|:|/:/  / \:\/:/  \/__/ \:\  \ /:/  / \:\/:/  \/__/ \:\/:/ /:/  / ")
time.sleep(.1)
print("     |:/:/  /   \::/__/       \:\  /:/  /   \::/__/       \::/ /:/  /  ")
time.sleep(.1)
print("     |::/  /     \:\  \        \:\/:/  /     \:\  \        \/_/:/  /   ")
time.sleep(.1)
print("     |:/  /       \:\__\        \::/  /       \:\__\         /:/  /    ")
time.sleep(.1)
print("     |/__/         \/__/         \/__/         \/__/         \/__/     ")
time.sleep(.7)
print(" ")
print("     *****    **                                                                 ***           * ***                                                                            **    ")
time.sleep(.1)
print("  ******  *  **** *                                                            ** ***        *  ****  *     *         *                                                          **   ")
time.sleep(.1)
print(" **   *  *   *****                                                            **   ***      *  *  ****     ***       **     **                                                   **   ")
time.sleep(.1)
print("*    *  *    * *                                                              **           *  **   **       *        **     **                                                   **   ")
time.sleep(.1)
print("    *  *     *                ***  ****       ****       ****         ****    **          *  ***                   ********  **    ***    ****                ***  ****          **   ")
time.sleep(.1)
print("   ** **     *         ***     **** **** *   * ***  *   * **** *     * ***  * ******     **   **          ***     ********    **    ***     ***  *    ****     **** **** *   *** **   ")
time.sleep(.1)
print("   ** **     *        * ***     **   ****   *   ****   **  ****     *   ****  *****      **   **   ***     ***       **       **     ***     ****    * ***  *   **   ****   ********* ")
time.sleep(.1)
print("   ** ********       *   ***    **         **    **   ****         **    **   **         **   **  ****  *   **       **       **      **      **    *   ****    **         **   ****  ")
time.sleep(.1)
print("   ** **     *      **    ***   **         **    **     ***        **    **   **         **   ** *  ****    **       **       **      **      **   **    **     **         **    **   ")
time.sleep(.1)
print("   ** **     **     ********    **         **    **       ***      **    **   **         **   ***    **     **       **       **      **      **   **    **     **         **    **   ")
time.sleep(.1)
print("   *  **     **     *******     **         **    **         ***    **    **   **          **  **     *      **       **       **      **      **   **    **     **         **    **   ")
time.sleep(.1)
print("      *       **    **          **         **    **    ****  **    **    **   **           ** *      *      **       **       **      **      *    **    **     **         **    **   ")
time.sleep(.1)
print("  ****        **    ****    *   ***         ******    * **** *      ******    **            ***     *       **       **        ******* *******     **    **     ***        **    **   ")
time.sleep(.1)
print(" *  *****      **    *******     ***         ****        ****        ****     **             *******        ****     **        *****   *****       ***** **     ***        ******     ")
time.sleep(.1)
print("*     **              *****                                                  **                 ***          ***                                     ***   **                ***      ")
time.sleep(.1)
print("*                                                                                                                                                                                     ")
time.sleep(.1)
print(" **                                                                                                                                                                                   ")
time.sleep(3)

while SelectScreen == "1":
    
    print("Hello & welcome to the world of Gitward!")
    #SelectScreen = getch() 
    
    if SelectScreen == "1":
        name= input("What is your name adventurer? \n")
        #name = "Zach"
        print("Hello,", name)
        print("Lets get started", name)
        time.sleep(2)
        cls()
        time.sleep(.5)
        while room != 4:
            oldroom = room
            print("You see", pathways, "pathways", paths, " \nWhat direction would you like to proceed in? \n")
            firstinput = getch()
            if firstinput.upper() == "N":
                room = room*5
                
            elif firstinput.upper() == "E":
                room = room*2
               
            elif firstinput.upper() == "S":
                room = room /5
            
            elif firstinput.upper() == "W":
                room = room /2
            if room == 1:
                roomname = "Mountain"
                paths = "N(Hospital),E(Hallway)"
                pathways = 2
                cls()
                if keys == 0:
                    while climb != "1" and climb != "2":
                        try:
                            print("Would you like to climb the mountain? \n [1] Yes [2] No")
                            climb = getch()
                            if climb == "1":
                                print("You found a key!! but... you lost 25 Health while doing so")
                                keys = 1
                                health = health - 25
                            elif climb == "2":
                                print("Goodbye")

                        except:
                            print("Invalid character")
                else:
                    print("You have alerady climbed the mountain")
            elif room == 2:
                roomname = "Hallway"
                paths = "N(Start),E(Boss Room),W(Mountain)"
                pathways = 2
            elif room == 4:
                roomname = "Bossroom"
                paths = "N(Weapons Room),W(Hallway)"
                pathways = 2
                cls()
                if len(inventory) != 0:
                    print("Would you like to fight Octocat? \n [1] Yes [2] No")
                    bossfight = getch()
                    if bossfight == "1":
                        print("Okay then...")
                        print("What weapon would you like to use?")
                        i = 0
                        while i < len(inventory):
                            print("[",i,"]",weapons[inventory[i]],"| Damage:",damage[inventory[i]])
                            i = i + 1
                        try:
                            choosenweapon = int(getch())
                            print("You picked",weapons[inventory[choosenweapon]])
                        except:
                            print("Invalid option")
                        print("Starting fight...")
                        time.sleep(2)
                        while health > 0 and octocathealth > 0:
                            cls()
                            print(name,"'s Health:",health,"Octocat's Health:",octocathealth)
                            time.sleep(2)
                            playerdamage = random.randint(damage[inventory[choosenweapon]]-5,damage[inventory[choosenweapon]]+2)
                            print(name,"hits octocat with",weapons[inventory[choosenweapon]],"and did",playerdamage,"damage!")
                            time.sleep(2)
                            octocathealth = octocathealth - damage[inventory[choosenweapon]]
                            octocatdamage = random.randint(1,30)
                            print("Octocat hits",name,"with his octopus like arms and did",octocatdamage,"damage!")
                            health = health - octocatdamage            
                            time.sleep(2)
                            
                        if octocathealth >health:
                            print("Octocat won...")
                            print("You Lose :(")
                        else:
                            print(name,"won!!! Congratulations!")
                            time.sleep(2)
                            cls()
                            print("8888888 8888888888 8 8888        8 8 888888888888    8 888888888888 b.             8 8 888888888o.      ")
                            time.sleep(.1)
                            print("      8 8888       8 8888        8 8 8888            8 8888         888o.          8 8 8888    `^888.   ")
                            time.sleep(.1)
                            print("      8 8888       8 8888        8 8 8888            8 8888         Y88888o.       8 8 8888        `88. ")
                            time.sleep(.1)
                            print("      8 8888       8 8888        8 8 8888            8 8888         .`Y888888o.    8 8 8888         `88 ")
                            time.sleep(.1)
                            print("      8 8888       8 8888        8 8 888888888888    8 888888888888 8o. `Y888888o. 8 8 8888          88 ")
                            time.sleep(.1)
                            print("      8 8888       8 8888        8 8 8888            8 8888         8`Y8o. `Y88888o8 8 8888          88 ")
                            time.sleep(.1)
                            print("      8 8888       8 8888888888888 8 8888            8 8888         8   `Y8o. `Y8888 8 8888         ,88 ")
                            time.sleep(.1)
                            print("      8 8888       8 8888        8 8 8888            8 8888         8      `Y8o. `Y8 8 8888        ,88' ")
                            time.sleep(.1)
                            print("      8 8888       8 8888        8 8 8888            8 8888         8         `Y8o.` 8 8888    ,o88P'   ")
                            time.sleep(.1)
                            print("      8 8888       8 8888        8 8 888888888888    8 888888888888 8            `Yo 8 888888888P'      ")
                            time.sleep(3)
                            print("\nAll programming done by: Zach Fauser")
                            time.sleep(2)
                            print("Special thanks to:")
                            time.sleep(2)
                            print("Visual Studio Code")
                            time.sleep(2)
                            print("Github")
                            time.sleep(2)
                            print("©2021 Fauser Consulting Inc. All rights reserved")
                            time.sleep(2)
                            print("Source Code: https://github.com/Zfauser/Heros-Of-Gitward")
                            time.sleep(60)
                            cls()
                        SelectScreen = "0"
                else:
                    print("You must have a weapon to fight Octocat!")
            elif room == 5:
                roomname = "Hospital"
                paths = "N(Monster Room),E(Start),S(Mountain)"
                pathways = 2
                health = 100
                print("Welcome To The Hosptal", name)
                print("You're now at 100 health again!")
            elif room == 10:
                roomname = "Start"
                paths = "N(Chest Room),E(Weapons Room),S(Hallway),W(Hospital)"
                pathways = 2
            elif room == 20:
                roomname = "Weapons Room"
                paths = "N(Guessing Game),S(Bossroom),W(Start)"
                pathways = 2
                cls()
                print("Welcome",name,"to the weapon's room!!")
                while option != 3:
                    print("You have",gold,"gold")
                    print("Would you like to [1] Buy [2] Sell [3] Leave")
                    option = int(getch())
                    if option == 1:
                        print("\nWhat weapon would you like to purchase?")
                        i = 0
                        try:
                            while i < len(weapons):
                                print("[",i,"]",weapons[i],"Cost:",cost[i],"Damage:",damage[i])
                                i = i + 1
                            print("[",i,"] Nothing")        
                            buy = int(getch())
                            if buy != i:
                                if gold - cost[buy] < 0:
                                    print("You don't have enough gold for that weapon")
                                else:
                                    gold = gold - cost[buy]
                                    inventory.append(buy)
                                    print("You bought",weapons[buy])

                        except:
                            print("Invalid option")
                    if option == 2:
                        if len(inventory) == 0:
                            print("\nYou don't have any weapons to sell \n")
                        else:
                            print("What weapon would you like to sell?")
                            i = 0
                            while i < len(inventory):
                                print("[",i,"]",weapons[inventory[i]],"| Worth:",cost[inventory[i]],"Gold | Damage:",damage[inventory[i]])
                                i = i + 1
                            print("[",i,"] Nothing")
                            try:
                                sell = int(getch())
                                if sell != i:
                                    gold = gold + cost[inventory[sell]]
                                    print("You sold",weapons[inventory[sell]],"+",cost[inventory[sell]],"gold")
                                    inventory.pop(sell)
                            except:
                                print("Invalid option")
                    if option == 3:
                        print("Bye",name,)
                option =0
            elif room == 25:
                roomname = "Monster Room"
                paths = "E(Chest Room),S(Hospital)"
                pathways = 2
                monsterdamage = random.randint(25,50)
                health=health-monsterdamage
                print("The monster attacked you! You lost",monsterdamage,"health")
            elif room == 50:
                roomname = "Chest Room"
                paths = "W(Monster room),E(Guessing game),S(Start)"
                pathways = 3
                cls()
                if keys == 1:
                    print("You have the Key! Would you like to open the chest? \n Press [1] To open or press [2] to not")
                    open = int(getch())
                    if open == 1:
                        amountofgold = random.randint(10,20)
                        gold = gold + amountofgold
                        print("You got",amountofgold,"gold")
                else:
                    print("The chest is locked")

            elif room == 100:
                roomname = "Guessing Game"
                paths = "W(Chest Room),S(Weapons Room)"
                pathways = 2
                cls()
                if triviagames == 0:
                    print('Hello', name,("welcome to..."))
                    time.sleep(1.3)
                    print(" _______ __________________ _______ _________         _________ _______ ")
                    time.sleep(.1)
                    print("(  ____  \\__   __/\__   __/(  ____ )\__   __/|\     /|\__   __/(  ___  )")
                    time.sleep(.1)
                    print("| (    \/   ) (      ) (   | (    )|   ) (   | )   ( |   ) (   | (   ) |")
                    time.sleep(.1)
                    print("| |         | |      | |   | (____)|   | |   | |   | |   | |   | (___) |")
                    time.sleep(.1)
                    print("| | ____    | |      | |   |     __)   | |   ( (   ) )   | |   |  ___  |")
                    time.sleep(.1)
                    print("| | \_  )   | |      | |   | (\ (      | |    \ \_/ /    | |   | (   ) |")
                    time.sleep(.1)
                    print("| (___) |___) (___   | |   | ) \ \_____) (___  \   /  ___) (___| )   ( |")
                    time.sleep(.1)
                    print("(_______)\_______/   )_(   |/   \__/\_______/   \_/   \_______/|/     \|")
                    time.sleep(3)
                    cls()
                    print("There will be 5 multiple choice questions for each question you get correct you will get +2 gold.")
                    print("With all that said lets get started!!\n\n")
                    question = [
                        "What is the name of Adobe's programming language? \n 1 C++ \n 2 Java \n 3 ColdFusion \n 4 Python",
                        "What is Microsoft's cloud platform? \n 1 Microsoft Cloud \n 2 Microsoft Azure \n 3 Microsoft Web Services \n 4 Microsoft Sky", 
                        "What opeating system has a penguin as it's logo? \n 1 MacOS \n 2 Windows \n 3 Android \n 4 Linux", 
                        "What year was Adobe Dreamweaver introduced? \n 1 1997 \n 2 2006 \n 3 1987 \n 4 2016", 
                        "What is the best selling personal computer of all time? \n 1 The Apple Lisa \n 2 The Commodore 64 \n 3 Apple II \n 4 The Tandy TRS-80"
                        ]

                    answer = ["3","2","4","1","2"]
                    questionnum = 0
                    while questionnum <5:
                        print(question[questionnum], "\n Please enter 1,2,3, or 4")
                        firstquestion = getch()

                        if firstquestion == answer[questionnum]:
                            print("You are correct! +2 gold")
                            gold=gold+2
                            questionnum=questionnum+1

                        elif firstquestion == "1" or firstquestion == "2" or firstquestion == "3" or firstquestion == "4":
                            print("Incorrect the answer was:", answer[questionnum])
                            questionnum=questionnum+1
                        else:
                            cls()

                        print("Gold:",gold,"\n")
                    triviagames=1

                else:
                    print("You have alerady played GiTriva!")

            elif room == 0.4:
                roomname = "Secret"
                if foundsecret == 0:
                    print("You have found the secret room! +10 Gold")
                    #sys.stdout.write('\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a')
                    foundsecret = 1
                    gold = gold+10
                paths = "N(Hallway)"
                pathways = 1
            else:
                roomname = "Not Allowed"
                room = oldroom
            beep()
            print("You're now in the",roomname,(","),name)
            print("Gold:",gold,"Health:",health)
            if health==0:
                print("Dead")
                break