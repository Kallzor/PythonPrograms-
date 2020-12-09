"""I denna laboration ska vi implementera en enkel ordlista m.h.a. python.
Ordlistan ska vara interaktiv och användaren ska kunna lägga till och slå upp ord i ordlistan.
Själva ordlistan ska implementeras på tre olika sätt, med tre olika sätt att spara ordlistan.
Följande tre olika sätt att lagra en ordlista implementeras:

Två stycken listor av strängar. Den första listan innehåller ordet vi vill slå upp, och den andra
listan innehåller beskrivningen för det ordet, på motsvarande position.
En lista av tupler. En enda lista som består av par, där första delen av varje par är ordet vi vill
slå upp, och den andra är beskrivningen. Observera här altlså att datastrukturen ska vara  en lista,
 varje element i denna lista ska i sin tur vara ett par (en tupel med två element).
Ett dictionary. Ett dictionary som innehåller ordet vi vill slå upp som "nyckel" och tillhörande
beskrivning som "värde".
För varje lösning ska två operationer finnas: en för att sätta in och en för att slå upp ord i listan.
Varje operation ska implementeras som en egen funktion för att ge programmet bra struktur. Återanvänd
gärna kod mellan de tre lösningarna (t.ex. kan du ha samma funktion som skriver ut själva menyn).

Separera de tre lösningarna genom att välja olika namn på funktionerna för respektive operation. Varje
lösning ska dessutom ha en egen funktion som startar just den lösningen.

Ordlistan ska presentera användaren med en meny där det finns följande alternativ: 1: Insert, 2: Lookup.
Användaren ska kunna välja alternativ genom mata in siffran för motsvarande operation. Programmet ska sedan
fråga användaren efter vilket ord operationen ska verka på och sedan, i fallet med insert fråga efter ordets
beskrivning. Det ska inte vara tillåtet att sätta in samma ord två gånger i ordlistan. Om användaren försöker
göra det ska ett felmeddelande skrivas ut. I fallet med lookup ska beskrivningen för ordet, som finns lagrad,
 skrivas ut på skärmen. Om ordet som slås upp inte existerar i ordlistan så ska ett felmeddelande skrivas ut.
"""

import sys
import termcolor


def MenuOptions():  #prints menu
    print("1: add")
    print("2: lookup")
    print("3: see your dictionary")
    print("4: exit program")
    Option = input("Which option do you chose?: ")
    return Option  #returns choice of action.


def Add(Dict):  #Adds key-word and value to set key.
    Word = input("What word do you want to add?: ")
    if Word in Dict:
        print("This word already exist!")  #checks if key already exists.
    else:
        Meaning = input("What is the meaning of set word?: ")
        Dict[Word] = Meaning




def LookUp(Dict):  #Prints out the meaning the inputed word.
    Word = input("Word to lookup : ")
    print("\n")
    if Word not in Dict:
        print("This word does not exists")
    else:
        print(Dict[Word])


def See(Dict): #Prints out dict.
    print(Dict)



def Exit(Dict):  #Sub exit function.
    print(termcolor.colored("Have an amazing day and I hope you're doing great! :) See you next time!", "blue"))
    sys.exit()



def Switch_Menu(argument, Dict):  #Calling upon function depending on input.
    Switcher = {
        "1": Add,
        "2": LookUp,
        "3": See,
        "4": Exit
    }
    if argument in Switcher:
        func=Switcher.get(argument)
        func(Dict)
    else:
        print("Stop pressing on random buttons >:(")


def Run(): #Starts program
    Dict = {}
    while 1:
        x = MenuOptions()
        Switch_Menu(x, Dict)


Run()