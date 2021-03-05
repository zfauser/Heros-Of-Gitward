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
controls= ("Controls: \nTo move forward use: f \nTo move backwards use: b \nTo move left use: l \nTo move right use: r \nTo climb up use: C \nTo climb down use: d \nTo attack use: a \nTo open something use: o \nTo see this menu again use: ? \n")
triviagames = 0
gold = 0
room = 10
foundsecret = 0
roomname = "start"
health = 100
while True:
    #print("Hello & welcome to the world of Gitward! \nWould you to (1) play or (2) see the controls? \nPlease enter 1 or 2 below \n")
    #SelectScreen = getch() 
    SelectScreen = "1"
    if SelectScreen == "1":
        #name= input("What is your name adventurer? \n")
        name = "Zach"
        #print("Hello,", name)
        #print("Lets get started", name)
        #time.sleep(2)
        #print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        #time.sleep(1)
        while room != 4:
            oldroom = room
            print("You see", pathways, "pathways", paths, " \nWhat direction would you like to proceed in? \n")
            firstinput = getch()
            if firstinput == "?":
                print(controls)
            elif firstinput.upper() == "N":
                room = room*5
                
            elif firstinput.upper() == "E":
                room = room*2
               
            elif firstinput.upper() == "S":
                room = room /5
            
            elif firstinput.upper() == "W":
                room = room /2
            if room == 1:
                roomname = "Mountain"
                paths = "N,E"
                pathways = 2
            elif room == 2:
                roomname = "Hallway"
                paths = "N,E"
                pathways = 2
            elif room == 4:
                roomname = "Bossroom"
                paths = "N,E"
                pathways = 2
                print("You win")
                break
            elif room == 5:
                roomname = "Hospital"
                paths = "N,E"
                pathways = 2
                health = 100
                print("Welcome To The Hosptal", name)
                print("You're now at 100 health again!")
            elif room == 10:
                roomname = "Start"
                paths = "N,E"
                pathways = 2
            elif room == 20:
                roomname = "Weapons Room"
                paths = "N,E"
                pathways = 2
            elif room == 25:
                roomname = "Monster Room"
                paths = "N,E"
                pathways = 2
                health=health-random.randint(25,50)
            elif room == 50:
                roomname = "Chest Room"
                paths = "N(monster room),E(guessing game),S(Start)"
                pathways = 3
            elif room == 100:
                roomname = "Guessing Game"
                paths = "N,E"
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
                paths = "N"
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
        
    
    if SelectScreen == "2":
        print(controls)
