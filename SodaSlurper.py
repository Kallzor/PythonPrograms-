def SodaSlurper():
    x, y, z = map(int, input().split())
    emptyCans = x + y
    counter = 0
    while emptyCans >= z:
        emptyCans -= z
        counter += 1
        emptyCans += 1
    print(counter)

SodaSlurper()
