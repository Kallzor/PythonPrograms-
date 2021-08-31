def Modulo():
    List = []
    for i in range(10):
        x = int(input())
        x = x % 42
        List.append(x)

    List = set(List)
    print(len(List))

Modulo()
