import sys
import termcolor

def MenuOptions():
    print("1: add")
    print("2: lookup")
    print("3: see your tuple")
    print("4: exit program")
    Option = input("Which option do you chose?: ")
    return Option

def Add(Listkey):  #Adds new word and meaning to the tuple.
    Word = input("What word do you want to add: ")
    if IsDuplicate(Listkey, Word):
        print("Word already exists")
    else:
        Meaning = input("What is the meaning of set word: ")
        Listkey.append((Word, Meaning))

def IsDuplicate(Listkey, Word):  #Checks if word already exists in tuple.
    for i in range(len(Listkey)):
        if Listkey[i][0] == Word:
            return True
    return False

def LookUp(Listkey):  #Prints out the meaning of inputed word.
    Word = input("What word do you want to look up?: ")
    print("\n")
    if not IsDuplicate(Listkey, Word):
        print("Word does not exists")
    else:
        for i in range(len(Listkey)):
            if Listkey[i][0] == Word:
                print(Listkey[i][1])

def See(Listkey):  #Prints out all tuples.
    for i in range(len(Listkey)):
        print(Listkey[i])

def Exit(Listkey):  #Sub exit function
    print(termcolor.colored("Have an amazing day and I hope you're doing great! :) See you next time!", "blue"))
    sys.exit()

def switch_menu(argument, Listkey):  #Calling upon function depending on input.
    switcher = {
        "1": Add,
        "2": LookUp,
        "3": See,
        "4": Exit
    }
    if argument in switcher:
        func=switcher.get(argument)
        func(Listkey)
    else:
        print("You need to stop pressing random buttons >:(")




def run(): #Starts program
    Listkey = []
    while 1:
        x = MenuOptions()
        switch_menu(x, Listkey)

run()
