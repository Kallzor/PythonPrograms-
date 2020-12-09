"""Some dumbfuck about a pet and some shit about wanting to hide etc.
Use circle to code a way that the first input is = or > than first input"""

import math

def circle():
    x,y = list(map(float, input().split()))
    r = math.sqrt(x/(math.pi))
    if (2*math.pi*r) > y:
        print("Need more materials!")
    else:
        print("Diablo is Happy!")

circle()
