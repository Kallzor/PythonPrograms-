def Save():
    x, y = map(int, input().split())
    Lst = list(range(0, x))
    for i in range(y):
        Remove = int(input())
        if Remove in Lst:
            Lst.remove(Remove)
    print(*Lst, sep = "\n")
    print("Mario got " + str(x - len(Lst)) + " of the dangerous obstacles.")

Save()