"""En telefonbok
Glöm inte att beakta kodstilen i denna lab. Denna laboration syftar till att öva användning av
 dictionaries och objekt (även om detta inte är ett krav), i synnerhet vad gäller hantering av alias.
 Dessutom kommer programmet som ska skrivas att vara interaktivt. Viss rudimentär felhantering kommer också att
  behövas, men om detta ska implementeras med hjälp av Python's exceptions är en designfråga där beslutet är ert eget.

Laborationsuppgiften är att skriva ett interaktivt program som hanterar en dynamisk telefonbok via en
uppsättning enkla kommandon (dynamisk betyder att det går att ändra i telefonboken). Kommandona ska alla
vara en rad långa och kunna updelas i ord med whitespace emellan (ett eller flera whitespace ska accepteras
 av programmet).  Telefonboken kan antingen användas till gamla hederliga fasta telefoner (Links to an external site.)
  (en antik företeelse som existerade förra seklet) eller till att hantera mer moderna mobiltelefoner
  (Links to an external site.) som har tvillingkort (där då fler telefoner får samma nummer). Prompten kan
  vara helt valfri (prompt=det som skrivs ut innan programmet väntar på inmatning från användaren). Följande
   kommandon ska hanteras (fler får läggas till efter behag):

add name number – lägger till name med nummret number till telefonboken. Här är det tillåtet att begränsa sig
till att namn måste vara unika (två olika personer med olika nummer kan inte heta likadant). Alla telefonnummer
 måste vara unika; det är alltså inte tillåtet att lägga till flera namn med samma telefonnummer som inte är alias
 (alias har alltid, per konstruktion, samma telefonnummer).
lookup name – skriver ut numret som finns lagrat för name.
alias name newname – låter name bli sökbart även under namnet newname. Observera att name och newname blir helt
likställda - newname fungerar i alla avseenden som name.
change name number – ändrar numret som associeras med det befintliga namnet name till number.
save filename – sparar innehållet i telefonboken till filen filename.
load filename – läser in innehållet från filen filename till telefonboken. Telefonboken i minnet kastas bort
(efter inläsningen har vi endast telefonboken från filen i minnet).
quit – avslutar den interaktiva körningen
För kommandot add gäller att en felutskrift ska genereras om name redan finns definierat i telefonboken; för
de övriga gäller att felutskrift ska ske om name inte är definierat. Med felutskrift menas att programet ska
berätta vad som är fel på ett begripligt sätt och sedan skriva ut prompten igen. Namn som definierats som alias
 (med alias-kommandot) ska kunna användas i lookup-, change- och andra alias-kommandon på samma sätt som alla namn,
  så att följande beteende erhålls:

telebok> add peter.forsberg 12345
telebok> lookup peter.forsberg
12345
telebok> alias peter.forsberg foppa
telebok> lookup foppa
12345
telebok> alias foppa MR21
telebok> change MR21 67890
telebok> lookup peter.forsberg
67890

Notera att programmet ska presentera en prompt ("telebok>" i det här fallet") och att användaren
 sedan ska kunna skriva ovanstående kommandon på beskrivet sätt. Det är inte tillåtet att ha en meny i denna uppgift.
Ett telefonnummer lagras lämpligtvis som en sträng. Ingen speciell kontroll av formatet på telefonnumret
behöver göras (om användaren är dum nog att skriva in nåt annat än ett telefonnummer så tillåts det också).
Ytterligare ett textexempel med en sparfil finns.
Load och save (filformat) - förenklad version:
Det är tillåtet att ignorera alias när man sparar till och laddar från fil. Filformatet är som följer:
 På varje rad i filen ska ett telefonnummer sparas först på raden, åtföljt av ett semikolon och sedan
 åtföljt av namnet som motsvarar telefonnumret fölt av semikolon. Om det alltså råkar finnas alias för
 namnet så sparar man detta på en egen rad, fast med samma telefonnummer. Vi får då en rad per namn i
 filen (ingen skillnad på "namn" och "alias"). Man behöver då inte ta hänsyn till alias när man sparar,
 vilket förenklar en hel del. När man laddar in en sådan fil (använder load) får man naturligtvis inte
 tillbaka aliasen, utan varje namn upptäder då i telefonboken som ett eget namn med eget telefonnummer
 (som råkar vara samma telefonnummer som någon anna, som tidigare var alias). Exempel (samma telefonbok som ovan):

123;Kalle;
123;Maria;
321;Anna;
321;Olle;

Internt i programmet är det lämpligt att använda ett dictionary som central datastruktur. Det finns dock all
anledning att inte låta detta dictionary lagra telefonnummer direkt som värde, utan att blanda in muterbara
datastrukturer (t ex objekt) som mellansteg (detta är den enklaste lösningen). Det är
också starkt rekommenderat att inte göra någon skillnad överhuvudtaget på namn och alias;
ett alias är bara ett till namn för samma nummer. Det interaktiva beteendet åstadkoms enklast genom att en
loop (lämpligen while) börjar varje varv med att anropa input(), varefter resultatet analyseras och motsvarande
 kommando utförs (tänk på att detta inte går att göra rekursivt, eftersom vi potentiellt kör gopdtyckligt många
  varv, vilket skulle fylla upp minnet). Försök separera ut kommandon så att dessa implementeras
  i separata funktioner."""

import sys

def MenuOptions():  #prints menu
    Option = input("telebok> ")
    if Option == "quit":
        sys.exit()
    return Option  #returns choice of action.


def Add(Name,Number,DictName):
    if Name in DictName:
        print("The thing you wanted to add already exists")
    elif IsDuplicate(Number, DictName):  #Checks if number already exist.
        print("This number already exist")
    else:
        DictName[Name] = Number


def LookUp(Name, DictName):
    if Name not in DictName:
        print("This thing does not exist")
    else:
        print(DictName[Name])


def ChangeValue(Name, NewNumber, DictName):
    if Name not in DictName:
        print("This word does not exist")
    elif IsDuplicate(NewNumber, DictName):  #Calls upon duplicate function.
        print("This number already exist")
    elif Name in DictName:
        x = DictName[Name]
        for i in DictName:
            if x == DictName[i]:
                DictName[i] = NewNumber


def Save(DictName):  #Saves as txt file.
    with open(input("What do you want to save your file as? "), "w") as f:
        for i in DictName:
            f.write(DictName[i] + ";" + i + ";" + "\n")


def Load(DictName):  #Loads existing txt file.
    f = open(input("What file do you want to load?: "))
    for i in f:
        x = i.split(";")
        DictName[x[1]] = x[0]

def Alias(Name, NewAlias, DictName):
    if Name not in DictName:
        print("This name does not exist")
    elif NewAlias in DictName:
        print("This name already exist")
    elif IsDuplicate(Name, DictName):
        print("This number already exist")
    else:
        DictName[NewAlias] = DictName[Name]


def IsDuplicate(Number, DictName):  #Checks if number already exist.
    for i in DictName:
        if DictName[i] == Number:
            return True
    return False


def Switch_Menu(argument, DictName):  #Calling upon function depending on input.
    Switcher = {
        "add": Add,
        "lookup": LookUp,
        "change": ChangeValue,
        "save": Save,
        "load": Load,
        "alias": Alias
    }
    x = argument.split()
    if x[0] in Switcher:  #Checks if first argument exists in switcher.
        if len(x) > 3:  #No command needs    more than 3 arguments. Hence the limit is set to 3.
            print("too many arguments")
        if len(x) == 1:
            try:  #Tries to run, if program doesn't work, prints out error instead of crashing program.
                func = Switcher.get(x[0])
                func(DictName)
            except:
                print("Wrong amount of arguments")
        elif len(x) == 2:
            try:
                func = Switcher.get(x[0])
                func(x[1], DictName)
            except:
                print("Wrong amount of arguments")
        else:
            try:
                func=Switcher.get(x[0])
                func(x[1], x[2], DictName)
            except:
                print("Wrong amount of arguments")
    else:
        print("Stop pressing on random buttons >:(")


def Run():  #Starts the program
    DictName = {}
    while 1:
        x = MenuOptions()
        Switch_Menu(x, DictName)


Run()
