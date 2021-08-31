def HarshadNum():
    x = int(input())
    while x % sum(list(map(int, list(str(x))))) != 0:
        x += 1
    print(x)


HarshadNum()

