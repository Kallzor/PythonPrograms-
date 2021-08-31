def DiceGame():
    x = list(map(int, input().split(" ")))
    y = list(map(int, input().split(" ")))
    if sum(x) > sum(y):
        print("Gunnar")
    elif sum(x) == sum(y):
        print("Tie")
    else:
        print("Emma")

DiceGame()