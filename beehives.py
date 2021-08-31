def beehives():
    while True:
        sour = 0
        sweet = 0
        num = list(map(float, input().split()))
        variable = int(num[1])
        if num[-1] == 0:
            break
        for i in range(variable):
            data = list(map(float, input().split()))
            if abs(data[0] - data[1]) == 0:
                sweet += 1
            elif abs(data[1] - data[0]) < num[0]:
                sour += 1
            elif abs(data[1] - data[0]) > num[0]:
                sweet += 1
        print(str(sour) + " sour, " + str(sweet) + " sweet")

beehives()


"Vad i hevlete? Uppgiften är ju förfan dum i huvudet. Koden funkar om man faktiskt läser var uppgiften säger???"



