def Outlets(n):
    for i in range(n):
        x = list(map(int, input().split()))
        Num = 0
        Num += sum(x[1:])
        print(Num - x[0] + 1)

Outlets(int(input()))




