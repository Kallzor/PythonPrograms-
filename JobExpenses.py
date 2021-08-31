def Expenses():
    x = int(input())
    tot = 0
    z = map(int, input().split())
    for i in z:
        if i < 0:
            tot += i


    print(abs(tot))



Expenses()