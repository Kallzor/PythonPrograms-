"""Old MacDonald had a farm, and on that farm she had a square-shaped pasture, and on that pasture
 she had a cow that was prone to escape. So now Old MacDonald wants to set up a fence around the pasture.
 Given the area of the pasture, how long a fence does Old MacDonald need to buy?
Input
The input consists of a single integer a (1≤a≤1018), the area in square meters of Old MacDonald’s pasture.

Output
Output the total length of fence needed for the pasture, in meters. The length
should be accurate to an absolute or relative error of at most 10^−6."""

import math

print("{0:.6f}".format(4 * math.sqrt(int(input()))))

