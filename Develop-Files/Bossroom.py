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
weapons = ["Iron Sword","Battle Axe","Fire Rod","Crossbow"]
damage = [10,15,20,25]
inventory = [0,1,2,3]
name = "Zach"
octocathealth = 100
health = 100
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
else:
    print("You must have a weapon to fight Octocat!")