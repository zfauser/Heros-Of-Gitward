# https://github.com/Zfauser/Python-Game-Gr-9
import time
#import title
#getch from: https://stackoverflow.com/questions/27750536/python-input-single-character-without-enter
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
paths = "N(chestroom),E(weapons room),S(hallway),W(hospital)"
pathways = 4
controls= ("Controls: \nTo move forward use: f \nTo move backwards use: b \nTo move left use: l \nTo move right use: r \nTo climb up use: C \nTo climb down use: d \nTo attack use: a \nTo open something use: o \nTo see this menu again use: ? \n")
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
                health=health-50
            elif room == 50:
                roomname = "Chest Room"
                paths = "N(monster room),E(guessing game),S(Start)"
                pathways = 3
            elif room == 100:
                roomname = "Guessing Game"
                paths = "N,E"
                pathways = 2
            elif room == 0.4:
                roomname = "Secret"
                if foundsecret == 0:
                    print("You have found the secret room! +10 Gold")
                    foundsecret = 1
                    gold = gold+10
                paths = "N"
                pathways = 1
            else:
                roomname = "Not Allowed"
                room = oldroom
            print("You're now in the",roomname,(","),name)
            print("Gold:",gold,"Health:",health)
            if health==0:
                print("Dead")
                break
        
    
    if SelectScreen == "2":
        print(controls)
