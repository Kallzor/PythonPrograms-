def baby():
    counter = 0
    x = int(input())
    pain = list(map(str, input().split(" ")))
    for i in range(x+1):
        if str(i) != pain[i - 1] and pain[i - 1] != "mumble":
            counter = 1
            break
    if counter == 1:
        print("makes sense")
    else:
        print("something is fishy")


baby()

#Code should work???
