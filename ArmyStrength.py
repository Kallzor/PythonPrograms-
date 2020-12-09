def War(n):
    for i in range(n):
        trash = input()
        x = list(map(int, input().split()))

        Godzilla = list(map(int, input().split()))
        Mecha = list(map(int, input().split()))

        if max(Godzilla) == max(Mecha):
            print("Godzilla")
        elif len(Godzilla) == 0 and len(Mecha) == 0:
            print("uncertain")
        elif max(Godzilla) > max(Mecha):
            print("Godzilla")
        else:
            print("MechaGodzilla")

War(int(input()))
