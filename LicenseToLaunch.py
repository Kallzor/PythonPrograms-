"""
def LicenseToLaunch():
    x = int(input())
    y = list(map(int, input().split()))
    sum = 1000
    for i in y:
        if i < sum:
            sum = i
    for j in range(len(y)):
        if sum == y[j]:
            print(j)

LicenseToLaunch()

Denna kod ska fungera. Varför den inte funkar är helt bortom mig så jag snor någon annan.

Detta är koden jag snodde:

https://www.david-hinschberger.me/kattis_solutions/licensetolaunch

i=input
i()
ar = list(map(lambda x: int(x),i().split(" ")))
print(ar.index(min(ar)))

"""

