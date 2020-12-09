def bus(n):
    for i in range(n):
        t = int(input())
        k = 0
        while t > 0:
            k += 0.5
            k = k * 2
            t -= 1
        print(int(k))

bus(int(input()))

