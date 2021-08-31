def simonsays(n):
    for i in range(n):
        x = input().split()
        if x[0] == "simon" and x[1] == "says":
            print("", *x[2:], sep=" ")
        else:
            print("")

simonsays(int(input()))
