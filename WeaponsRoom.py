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
name = "zach"
gold = 20
weapons = ["Wood Sword","Iron Sword","Battle Axe","Fire Rod","Crossbow"]
cost = [5,10,15,20,25]
damage = [10,20,30,35]
print("Welcome",name,"to the weapon's room!!")
print("Would you like to [1] Buy [2] Sell [3] Leave")
option = getch()
if option == 1:
    print("What weapon would you like to purchase?")
    for x in weapons:
        print(x)
if option == 2:
    print("What weapon would you like to sell?")

if option == 3:
    print("Bye",name,)