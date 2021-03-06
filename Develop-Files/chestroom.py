import time
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
keys = 1
gold = 0
cls()
if keys == 1:
    print("You have the Key! Would you like to open the chest? \n Press [1] To open or press [2] to not")
    open = int(getch())
    if open == 1:
        amountofgold = random.randint(10,20)
        gold = gold + amountofgold
        print("You got",amountofgold,"gold")
        print("Gold:",gold)
else:
    print("The chest is locked")
