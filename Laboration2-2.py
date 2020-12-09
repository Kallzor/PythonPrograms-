"""I denna laboration ska vi titta lite närmare på funktionsbegreppet och (i de två första deluppgifterna) begreppet
rekursion och iteration (iteration betyder att man ska använda en loop ("snurra")).

Skriv en funktion bounce(n) som givet ett naturligt tal (heltal >=0) n skriver ut alla tal från 0 till n på skärmen, först i
fallande och sedan i stigande ordning. Exempel:

bounce(4)
4
3
2
1
0
1
2
3
4
bounce(0)
0

Funktionen ska implementeras med hjälp av rekursion. Tips: ett komma i slutet på print-satsen undertrycker
det radbyte som annars sker efter varje utskrift."""
import math

def bounce(x):
    print(x)                #Prints the first variable (4) otherwise it will start with the print(x) after first x-1. Which will show 3.
    if x > 0:
        bounce(x - 1)         #I'm calling on the bouce function and if x > 0 it will take the variable - 1 and print out the new answer. Everytime it get x > 0 it will continue doing this.
        print(x)

#bounce(int(input()))


def bounce2(x):
    for i in range(-x, x + 1):
        print(abs(i))

#bounce2(int(input()))

"""Skriv en funktion, tvarsumman, som beräknar tvärsumman av ett 
naturligt tal (funktionen ska ta ett heltal som argument).

Med tvärsumman menas summan av alla siffror i talet i talbasen 10 (alltså så som vi vanligtvis skriver talet).

Problemet ska lösas med en rekursiv funktion. Här är det inte tillåtet att konvertera talet till en sträng först.

Ledning: ett naturligt tal kan delas upp i en sista siffra och det tal man får om man "tar bort" den sista siffran

(här är operatorerna % och / lämpliga att använda). Om det inte blir något kvar när sista siffran tagits bort är

lösningen enkel, i annat fall har man fått ett nytt tal vars tvärsumma är en del av det sökta svaret."""



def tvarsumman(n):
    if n > 0:
        return n % 10 + tvarsumman(n // 10)
    return 0

#print(tvarsumman(int(input())))


"""Skriv en funktion, tvarsumman2, som utför samma sak som funktionen i uppgift 3, men inte är rekursiv utan iterativ."""

def tvarsumman2(num):
    result = 0
    while (num > 0):
        result = result + num%10
        num = num//10 
    return result

#tvarsumman2(int(input()))

#def f(x):
    #return(x**2-1)      USED THIS WHEN I WANTED TO TEST THE CODE OUT FOR MYSELF :)


def derivate(f, x, h):
    result = (1/(2*h))*((f(x+h)) - f(x - h))
    return result

#derivative()

def solve(f,x0,h):
    x = x0
    while True:
        x1 = x - (f(x) / derivate(f, x, h))
        if abs(f(x)) < h:
            return x
        if derivate(f, x, h) == 0:
            return None
        if abs(x1-x) < h:
            return x
        x=x1
def funktest(x):
    return -x**2 + 5*x +6

#print(solve(math.sin, 1, 0.00000000001))
#print(solve(funktest,0,0.00000001))


#print(solve(f, 2, 0.00001))

#import d0009e_lab2_solveTest #This is only for the solve function.
#import d0009e_lab2_bounceTest
#import d0009e_lab2_sumTest







