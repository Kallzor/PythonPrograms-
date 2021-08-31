def NumberFun(x):
    for i in range(x):
        a,b,c = list(map(int, input().split()))
        if a + b == c:
            print("Possible")
        elif a - b == c or b - a == c:
            print("Possible")
        elif a * b == c:
            print("Possible")
        elif a / b == c or b / a == c:
            print("Possible")
        else:
            print("Impossible")



NumberFun(int(input()))
