"""Receptet som sockerkakans innehåller för en portion till 4 person är
3 st ägg, 3 dl strösocker, 2 tsk vaniljsocker, 2 tsk bakpulver, 3dl vetemjöl
75 g smör och 1 dl vatten, 10 g smör i formen och 0.75 dl ströbröd""" 

"""Jag vill skapa en funktion som räknar ut hur mycket ingredienser som behöves per person för att sedan kunna skapa 
en funktion där jag kan sätta in vilket nummer av människor jag vill i funktionen och få fram lösningen."""

n=int(input('any number you want: '))

if n == 0:
    print("NEJ DET GÅR ICKE")
else:

def ingredienser(n):
    ägg = round(0.75*n)
    strösocker = 0.75*n 
    vaniljsocker = 0.5*n
    bakpulver = 0.5*n
    vetemjöl = 0.75*n
    smör = 10 + 18.75*n
    vatten = 0.25*n
    ströbröd = 0.75
    hurmångaäggochskit = "För att baka denna kaka så behövs det {} ägg, {} dl strösocker, {} tsk vaniljsocker, {} tsk bakpulver, {} dl vetemjöl, {} g smör varav 10 g är till formen, {} dl vatten och 0.75 dl ströbröd."
    print(hurmångaäggochskit.format(ägg, strösocker, vaniljsocker, bakpulver, vetemjöl, smör, vatten, ströbröd))


ingredienser(n)



"""En funktion tidblanda(antal) som beräknar och returnerar tiden för att blanda 
smeten till en sockerkaka för antal personer. Tidsåtgången ska beräknas som 10 minuter fast tid 
(oavsett antal personer) samt dessutom ytterligare en minut för varje person kakan är avsedd för."""

def tid(n):
    t = 10 + 1*n
                 #Quick function using the static number 10 with the changable variable "n" showing how many minutes it takes to bake the cake.
    return t
   

print(tid(n))







"""En funktion tidgradda(antal) som beräknar och returnerar tiden 
för att grädda kakan, Tidsåtgången ska beräknas som 30 minuter fast tid 
(oavsett antal personer) samt dessutom ytterligare 3 minuter för varje person
kakan är avsedd för."""

def tidtvå(n):
    t = 30 + 3*n 
                           #Pretty much identical to the function above but instead of adding 1 minute per person it adds 3 minutes per person.
    return t

print(tidtvå(n))

print("Antalet minuter som behövs för att blanda smeten samt grädda kakan ")

print(tidtvå(n)+tid(n))

"""Skriv, i samma fil, ett script (huvudprogram) som skriver ut sockerkaksrecept till 4 och 7 personer på skärmen. 
Programmet ska alltså skriva ut två recept efter varandra. Här är det noga med att du skriver just ett script, 
inte en till funktion. Scriptet ska däremot använda din funktion från uppgift 3."""

def visa_recept(n):
     recept = ingredienser(n)

visa_recept(4)
visa_recept(7)
