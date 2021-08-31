def twonumbers():
    n = list(map(int, input().split()))
    n.sort()
    print(*n, sep=" ")


twonumbers()

