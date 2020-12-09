import os
import sys
import termcolor
def MenuOptionsAlpha():  #Menu options for all 3 different programs.
    print("1: lists")
    print("2: dictionary")
    print("3: tuples")
    print("4: exit program")
    Argument = input("What option would you like to chose?: ")
    return Argument


def Switch_Menu(Argument):  #Calling upon function depending on input.
    Switcher = {
        "1": "Laboration3Listor.py",
        "2": "Laboration3Dict.py",
        "3": "Laboration3Tuple.py"
    }
    if Argument in Switcher:
        cmd=Switcher.get(Argument)
        os.system(cmd)
    else:
        print("Stop pressing on random buttons >:(")


def Exit():  #Head exit function.
    print(termcolor.colored("Have an amazing day and I hope you're doing great! :) See you next time!", "blue"))
    sys.exit()

def Run():  #Start function.
    while 1:
        x = MenuOptionsAlpha()
        if x == "4":
            Exit()
        Switch_Menu(x)

Run()
