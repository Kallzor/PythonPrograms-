def Shopping():
    x, y = map(int, input().split())
    List = []
    SecondList = []
    for i in range(x):
        word = input().split(" ")
        for j in word:
            List.append(j)
    List.sort()
    counter = 0
    for k in range(len(List)):
        try:
            if List[k] == List[k+1]:
                counter += 1
            else:
                counter = 0
            if counter >= 3:
                SecondList.append(List[k])
        except IndexError:
            continue

    print(len(SecondList))
    for k in range(len(SecondList)):
        print(SecondList[k])


Shopping()


#KOD FUNKAR INTE MAD MAD MAD MAD
