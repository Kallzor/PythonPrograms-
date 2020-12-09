"""Input
The input starts with an integer n, where 1≤n≤100,
representing the number of gnome groups. Each of the n following lines
contains one group of gnomes, starting with an integer g, where 3≤g≤1000,
representing the number of gnomes in that group. Following on the same line are g
space-separated integers, representing the gnome ordering. Within each group all the integers
(including the king) are unique and in the range [0,10000]. Excluding the king, each integer is
exactly one more than the integer preceding it.

Output
For each group, output the king’s position in the group (where the first gnome in line is number one)."""

def Odd(n):
    for i in range(n):
        x = [int(z) for z in input().split()]
        y = x[0]
        x = x[1:]
        Meme = 0
        for i in range(y):
            Current = x[i]
            Previous = x[i - 1]
            if Current - Previous != 1:
                Meme = Current
        print(x.index(Meme))

Odd(int(input()))
