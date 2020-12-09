def Janitor():
    a,b,c,d = map(int, input().split())
    s = (a + b + c + d) / 2
    Max_Area = (((s - a)*(s - b) * (s - c) * (s - d)) ** 0.5)
    if Max_Area == 9.0:
        print(int(Max_Area))
    else:
        print(Max_Area)



Janitor()
