# https://github.com/Zfauser/Python-Game-Gr-9
import time
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
while True:
    SelectScreen = int(input("Hello & welcome to the world of Gitward! \nWould you to (1) play or (2) see the controls? \nPlease enter 1 or 2 below \n"))
    if SelectScreen == 1:
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
