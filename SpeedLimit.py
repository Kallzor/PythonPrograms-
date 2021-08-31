def speed():
    x = int(input())
    while x > 0:
        sum = 0
        pHour = 0
        for i in range(x):
            mph,hours = map(int, input().split())
            sum += (mph * (hours - pHour))
            pHour = hours
        if sum == 0:
            continue
        else:
            print(str(sum) + " miles")
        x = int(input())

speed()

