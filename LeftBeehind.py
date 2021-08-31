def bees():
    switch = True
    while switch:
        x,y = map(int, input().split())
        if x == 0 and y == 0:
            switch = False
        elif x + y == 13:
            print("Never speak again.")
        elif x > y:
            print("To the convention.")
        elif x < y:
            print("Left beehind.")
        elif x == y:
            print("Undecided.")


bees()
