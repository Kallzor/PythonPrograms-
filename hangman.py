def hangman():
    count = 0
    word = input()
    trueWord = list(set(word))
    gateList = []
    letters = input()
    for i in letters:
        if i in trueWord:
            gateList.append(i)

        if len(gateList) == len(trueWord):
            break

        if i not in trueWord:
            count += 1
            if count >= 10:
                print("LOSE")
                break
    if count < 10:
        print("WIN")


hangman()

"fyfan vad tid det här tog för ingen jävla anledning lol"
