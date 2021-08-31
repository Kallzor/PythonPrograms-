def StopWatch():
    x = int(input())
    result = 0
    if x/2 != x//2:
        print("still running")
    else:
        for i in range( x // 2):
            begin = int(input())
            stop = int(input())
            result += stop - begin
        print(result)

StopWatch()
