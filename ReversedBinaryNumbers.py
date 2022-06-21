


def binary():
    s = int(input())
    num = bin(s)
    reverse = num[-1:1:-1]
    reverse = reverse + (4 - len(reverse)) * '0'

    print(int(reverse, 2))

binary()


'''

x = int(input())

print(int("".join(list(str(bin(x)))[::-1][:len(list(str(bin(x))))-2]), 2))
'''