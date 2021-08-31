def homeWork():
    x = input()
    dumbfucklist = x.split(";")
    counter = 0
    for i in dumbfucklist:
        if "-" in i:
            fuckoffleo = i.split("-")
            counter += int(fuckoffleo[1]) - int(fuckoffleo[0]) + 1
        else:
            counter += 1
    print(counter)

homeWork()
