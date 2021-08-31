def fromatob():
    a,b = list(map(int, input().split()))
    counter = 0
    while a > b:
        if a%2 == 0:
            a = a/2
            counter += 1
        else:
            a = a + 1
            counter += 1
    if a < b:
        if abs(a - b) != 0:
            counter += b - a
            a = a + (b - a)
        if abs(a - b) == 0:
            print(int(counter))
    else:
        print(counter)


fromatob()
