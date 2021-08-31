def pet():
    tot = 0
    winner = 0
    for i in range(5):
        n = list(map(int, input().split()))
        if sum(n) > tot:
            tot = sum(n)
            winner = i
    print(str(winner + 1) + " " + str(tot))

pet()
