"""You are the CEO of Nasty Hacks Inc., a company that creates small pieces of malicious software which
 teenagers may use to fool their friends. The company has just finished their first product
 and it is time to sell it. You want to make as much money as possible and consider advertising
 in order to increase sales. You get an analyst to predict the expected revenue, both with and without advertising.
 You now want to make a decision as to whether you should advertise or not, given the expected revenues.
Input
The input consists of n cases, and the first line consists of one positive integer giving n.
The next n lines each contain 3 integers, r, e and c. The first, r, is the expected revenue if you do not advertise,
the second, e, is the expected revenue if you do advertise, and the third, c, is the cost of advertising.
You can assume that the input will follow these restrictions: 1≤n≤100, −106≤r,e≤106 and 0≤c≤106.

Output
Output one line for each test case: “advertise”, “do not advertise” or “does not matter”,
indicating whether it is most profitable to advertise or not, or whether it does not make any difference."""


def adver(n):
    for i in range(n):
        r,e,c = map(int, input().split())
        if (e - c) > r:
            print("advertise")
        elif (e - c) == r:
            print("does not matter")
        else:
            print("do not advertise")



adver(int(input()))








