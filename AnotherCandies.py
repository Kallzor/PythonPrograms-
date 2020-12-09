def Candies(n):
    for i in range(n):
        trash = input() #För att ta bort blank space
        godis = 0
        barn = int(input())
        for j in range(barn):
            AddCandy = int(input())
            godis += AddCandy
        if godis % barn == 0:
            print("YES")
        else:
            print("NO")


Candies(int(input()))
