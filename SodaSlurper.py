"""Some dumbfuck kid drinks some sodas. How many can he maximum drink that day?"""

def soda():
    x, y, z = list(map(int, input().split()))
    while 1:
        c = ((x+y)/z)   #c = totala tomma burkar/ hur många han behöver för att köpa en ny burk
        if c < 1:  #om c < 1 så kan han inte köpa någon mera burk.
            print(c) #c kommer vara antalet burkar han kan dricka den dagen
        elif c >= 1:
            if c/z > 1:
                NewC = 2