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
    for x in range(frequency):
        print("\a",end="\r")
        time.sleep(interval)
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
name = "Zach"
gold = 20
weapons = ["Iron Sword","Battle Axe","Fire Rod","Crossbow"]
cost = [10,15,20,25]
damage = [10,15,20,25]
inventory = [1,3]
option = 0
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
        
        
