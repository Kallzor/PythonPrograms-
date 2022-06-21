def eenymeeny():
    rhyme = input().split(" ")
    players = int(input())
    nameList = []
    for i in range(players):
        nameList.append(input())
    teamOne = []
    teamTwo = []
    previous = 0
    counter = 0
    while len(nameList) > 0:
        start = (previous + len(rhyme) - 1) % len(nameList)
        previous = start
        if counter == 0:
            teamOne.append(nameList[start])
            counter += 1
            nameList.pop(start)
        elif counter == 1:
            teamTwo.append(nameList[start])
            counter -= 1
            nameList.pop(start)

    print(len(teamOne))
    for j in teamOne:
        print(j)
    print(len(teamTwo))
    for y in teamTwo:
        print(y)

eenymeeny()