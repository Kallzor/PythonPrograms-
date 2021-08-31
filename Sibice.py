def Sibice():
    x, y, z = map(int, input().split())
    for i in range(x):
        if int(input())^2 <= (y^2) + (z^2):
            print("DA")
        else:
            print("NE")

Sibice()
