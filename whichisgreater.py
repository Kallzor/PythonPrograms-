# main.py for problem: whichisgreater
from sys import stdin

x = list(map(int, input().split()))

if x[0] > x[1]:
    print("1")
else:
    print("0")


