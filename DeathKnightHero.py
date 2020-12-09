def Fight(n):
    wins = 0
    for i in range(n):
        x = input()
        if "CD" not in x:
            wins += 1
    print(wins)

Fight(int(input()))
