import time
import os
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
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
gold = 0
questionnum = 0
triviagames = 0
name = "placeholder"
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
