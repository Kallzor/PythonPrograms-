def Swords():
    x = int(input())
    T = 0
    L = 0
    B = 0
    R = 0
    for i in range(x):
        y = input()
        y = [int(j) for j in y]
        if y[0] == 0:
            T += 1
        if y[1] == 0:
            B += 1
        if y[2] == 0:
            L += 1
        if y[3] == 0:
            R += 1
    totBT = T + B
    totLR = L + R
    totBuild = 0
    while totBT >= 2 and totLR >= 2:
        totBuild += 1
        totBT -= 2
        totLR -= 2
    print("{} {} {}".format(totBuild, totBT, totLR))

Swords()