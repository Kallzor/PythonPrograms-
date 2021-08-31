def ratingproblems():
    a,b = list(map(int, input().split()))
    z = a - b
    dumblist = []
    list1 = []
    for i in range(b):
        x = int(input())
        dumblist.append(x)
        list1.append(x)
    for i in range(z):
        dumblist.append(-3)
        list1.append(3)
    avgneg = sum(dumblist) / len(dumblist)
    avpos = sum(list1) / len(list1)
    print(avgneg, avpos)
ratingproblems()