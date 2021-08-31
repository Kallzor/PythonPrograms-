def foxxie(x):
    firstSTR = set("abcdefghijklmnopqrstuvwxyz")
    for i in range(x):
        secondSTR = set()
        thirdSTR = set()
        y = input().lower()
        for j in y:
            thirdSTR.add(j)
            if j in firstSTR:
                secondSTR.add(j)
        if len(secondSTR) == 26:
            print("pangram")
        else:
            print("missing", "".join(sorted(firstSTR - thirdSTR)))

foxxie(int(input()))
