"""Write a program that computes the difference between non-negative integers.

Input
Each line of the input consists of a pair of integers. Each integer is between 0 and 1015 (inclusive).
The input is terminated by end of file.

Output
For each pair of integers in the input, output one line, containing the absolute value of their difference."""
import sys

def different(a, b):
    result = abs(a - b)
    print(result)


for line in sys.stdin.readlines():
    a, b = map(int, line.split())
    different(a, b)

