def Surf():
    SPM = int(input())
    x = int(input())
    Total = 0
    for i in range(x):
        Spent = int(input())
        Total += SPM - Spent
    print(Total + SPM)

Surf()
