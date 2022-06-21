def oddecho():
    n = int(input())
    switch = 1
    for i in range(n):
        if switch == 1:
            print(input())
            switch += 1
        else:
            input()
            switch -= 1


oddecho()