"""You will be given three integers A, B and C. The numbers will not be given in that
exact order, but we do know that A is less than B and B less than C. In order to make
for a more pleasant viewing, we want to rearrange them in a given order.

Input
The first line contains the three positive integers A, B and C, not necessarily in that order.
The three numbers will be less than or equal to 100.

The second line contains three uppercase letters ’A’, ’B’ and ’C’ (with no spaces between them)
representing the desired order.

Output
Output A, B and C in the desired order on a single line, separated by single spaces."""

def Main():
    Num = list(map(int, input().split()))
    Order = list(input())
    Num.sort()
    if Order[0] == "A":
        Order[0] = Num[0]
    elif Order[0] == "B":
        Order[0] = Num[1]
    else:
        Order[0] = Num[2]
    if Order[1] == "A":
        Order[1] = Num[0]
    elif Order[1] == "B":
        Order[1] = Num[1]
    else:
        Order[1] = Num[2]
    if Order[2] == "A":
        Order[2] = Num[0]
    elif Order[2] == "B":
        Order[2] = Num[1]
    else:
        Order[2] = Num[2]
    print(*Order)


Main()

