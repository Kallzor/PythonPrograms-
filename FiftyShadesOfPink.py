def FiftySOP():
    x = int(input())
    sum = 0
    for i in range(x):
        word = input().lower()
        if "pink" in word or "rose" in word:
            sum += 1
    if sum == 0:
        print("I must watch Star Wars with my daughter")
    else:
        print(sum)


FiftySOP()
