def Bus():
    n = input()
    x = list(map(int, input().split()))
    x.sort()
    switcher = False
    min = 0
    max = 0
    for i in x:
        if x[i] + 1 == x[i + 1]:
            switcher = not switcher
            min = x[i]
        while switcher:
             if x[i] + 1 != x[i + 1]:
                 max = x[i]
    print(x)




Bus()
