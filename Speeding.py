def Speeding():
    x = int(input())
    maxSpeed = 0
    secondMax = 0
    for i in range(x):
        y = list(map(int, input().split()))
        if y[0] == 0:
            continue
        elif y[1] / y[0] > maxSpeed:
            secondMax = maxSpeed
            maxSpeed = y[1] / y[0]

    print((secondMax + maxSpeed))

Speeding()

#Denna kod borde funka. Vet inte vad som är problemet.
