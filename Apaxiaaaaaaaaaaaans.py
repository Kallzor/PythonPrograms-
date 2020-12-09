import itertools

def Apaxians():
    x = input()
    print("".join(c[0] for c in itertools.groupby(x)))

Apaxians()
