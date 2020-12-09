def Wonders():
    T = C = G = 0
    Cards = str(input())
    T = Cards.count("T")
    C = Cards.count("C")
    G = Cards.count("G")
    add = 0
    if T < C and T < G:
        add += 7 * T
    elif C < T and C < G:
        add += 7 * C
    elif G < T and G < C:
        add += 7 * G
    else:
        add += 7 * G
    print(T**2 + C**2 + G**2 + add)

Wonders()
