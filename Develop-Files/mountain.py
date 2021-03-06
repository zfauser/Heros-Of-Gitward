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
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
keys = 0
climb = 0
health = 100
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

