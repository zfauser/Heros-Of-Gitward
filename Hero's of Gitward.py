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
controls= ("Controls: \nTo move forward use: f \nTo move backwards use: b \nTo move left use: l \nTo move right use: r \nTo climb up use: C \nTo climb down use: d \nTo attack use: a \nTo open something use: o \nTo see this menu again use: ? \n")
gold = 0
points = 0
room = 10
roomname = "start"
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
            print("You see 4 pathways. \nWhat direction would you like to proceed in? \n")
            firstinput = getch()
            print(firstinput.upper())
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
            elif room == 2:
                roomname = "Hallway"
            elif room == 4:
                roomname = "Bossroom"
            elif room == 5:
                roomname = "Hospital"
            elif room == 10:
                roomname = "Start"
            elif room == 20:
                roomname = "Weapons Room"
            elif room == 25:
                roomname = "Monster Room"
            elif room == 50:
                roomname = "Chest Room"
            elif room == 100:
                roomname = "Guessing Game"
            elif room == 0.4:
                roomname = "Secret"
            else:
                roomname = "Not Allowed"
                room = oldroom
            print("You're now in the", roomname,(","),name)
        print("You win")
        break
    
    if SelectScreen == "2":
        print(controls)
