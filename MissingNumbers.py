def MissingNumbers():
    x = int(input())
    List = []
    for i in range(x):
        y = int(input())
        List.append(y)
    if len(List) == List[-1]:
        print("good job")
    else:
        for j in range(1, List[-1]):
            if j not in List:
                print(j)


MissingNumbers()

