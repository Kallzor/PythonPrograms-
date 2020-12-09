"""Write a program that, given a date in 2009, determines the day of week on that date.

Input
The first line contains two positive integers D (day) and M (month)
separated by a space. The numbers will be a valid date in 2009.

Output
Output the day of the week on day D of month M in 2009. The output should be one
of the words “Monday”, “Tuesday”, “Wednesday”, “Thursday”, “Friday”, “Saturday” or “Sunday”."""

import datetime

def Date():
    x = [int(z) for z in input().split()]
    d = x[0]
    m = x[1]
    y = datetime.datetime(2015, x[1], x[0])
    print(y.strftime("%A"))

Date()


