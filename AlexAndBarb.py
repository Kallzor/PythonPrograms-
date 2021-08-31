def AAB():
    x, y, z = map(int , input().split())
    counter = 0
    onOff = True
    while x > y and x > z:
        if onOff:
            if x > y:
                x -= y
                counter += 1
        if not onOff:
            if x > z:
                if y > x:
                    break
                else:
                    x -= z
                    counter += 1
    if counter % 2 == 0:
        print("Barb")
    else:
        print("Alex")

AAB()
