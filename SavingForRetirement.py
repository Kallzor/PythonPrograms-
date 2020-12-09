import itertools

def Save():
    x = list(map(int, input().split()))
    Bob = 0
    Alice = 0
    Bob =  (x[1] - x[0]) * x[2]
    for i in itertools.count():
        if Alice > Bob:
            print(x[3] + i)
            break
        else:
            Alice += x[-1]

Save()


