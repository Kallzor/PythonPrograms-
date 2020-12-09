"""You are hosting a party with G guests and notice that there is an odd number
of guests! When planning the party you deliberately invited only couples and gave
each couple a unique number C on their invitation. You would like to single out whoever
 came alone by asking all of the guests for their invitation numbers.

Input
The first line of input gives the number of cases, N. N test cases follow. For each test case there will be:

One line containing the value G the number of guests.

One line containing a space-separated list of G integers. Each integer C indicates the invitation code of a guest.

You may assume that 1≤N≤50,0<C<231,3≤G<1000.

Output
For each test case, output one line containing “Case #x: ” followed by the number C of the guest who is alone."""


def OddMan(n):
    for i in range(n):
        x = int(input())  #Onödig eftersom inte används. Endast där för att ta bort en input i princip xd
        z = list(map(int, input().split()))
        d = set()
        Remove = set(z)
        for j in z:
            if j in d:
                Remove.remove(j)
                d.remove(j)
            d.add(j)
        print("Case #{}: {}".format(i+1, Remove.pop()))


OddMan(int(input()))