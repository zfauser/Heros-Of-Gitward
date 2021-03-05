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
while True:
    print("Hello & welcome to the world of Gitward! \nWould you to (1) play or (2) see the controls? \nPlease enter 1 or 2 below \n")
    SelectScreen = getch() 
    if SelectScreen == "1":
        name= input("What is your name adventurer? \n")
        print("Hello,", name)
        print("Lets get started", name)
        time.sleep(2)
        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        time.sleep(1)
        while room==10:
            firstinput = input("You see 4 pathways. \nWhat direction would you like to proceed in? \n")
            if firstinput == "?":
                print(controls)
            elif firstinput.upper == "N":
                room+3
                print("You're now in room", 8,(","), name)
            elif firstinput.upper == "E":
                room+1
                print("You're now in room", room,(","), name)
            elif firstinput.upper == "S":
                room-3
                print("You're now in room", room,(","), name)
                break
    if SelectScreen == 2:
        print(controls)
