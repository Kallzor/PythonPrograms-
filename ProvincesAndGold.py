def Gold():

    g, s, c = map(int, input().split())

    bpg = g*3
    bps = s*2
    bpc = c
    bptot = bpg + bps + bpc

    if bptot >= 8:
        print("Province or Gold")
    elif bptot >=6:
        print("Duchy or Gold")
    elif bptot >=5:
        print("Duchy or Silver")
    elif bptot >= 3:
        print("Estate or Silver")
    elif bptot >= 2:
        print("Estate or Copper")
    else:
        print("Copper")

Gold()