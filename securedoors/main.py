def securedoors(x):
    insideList = []
    for i in range(x):
        enter = input().split(" ")
        if enter[0] == "entry":
            if enter[-1] in insideList:
                print(enter[-1] + " entered (ANOMALY)")
            else:
                insideList.append(enter[-1])
                print(enter[-1] + " entered")
        else:
            if enter[0] == "exit":
                if enter[-1] in insideList:
                    print(enter[-1] + " exited")
                    insideList.remove(enter[-1])
                else:
                    print(enter[-1] + " exited (ANOMALY)")

securedoors(int(input()))


