from collections import Counter
import itertools

def Count():
    Names = []
    for i in itertools.count():
        x = input()
        if x == "***":
            if sorted(lst[0]) == sorted(lst[1]):
                print("Runoff!")
            else:
                print(sorted(lst)[0])
        Names.append(x)
        NameCounter = Counter(Names)
        Max_Names = max(NameCounter.values())
        lst = [i for i in NameCounter.keys() if NameCounter[i] == Max_Names]

Count()



