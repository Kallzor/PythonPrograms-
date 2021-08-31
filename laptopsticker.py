def laptopsticker():
    n = list(map(int, input().split()))
    if n[0] - n[2] < 1 or n[1] - n[3] <= 1:
        print(0)
    else:
        print(1)

laptopsticker()
