"""It is Greg’s birthday! To celebrate, his friend Sam invites Greg and two other friends for a small party. 
Of course, every birthday party must have cake.

Sam ordered a square cake. She makes a single horizontal cut and a single vertical cut. 
In her excitement to eat cake, Sam forgot to make these cuts through the middle of the cake.

Of course, the biggest piece of cake should go to Greg since it is his birthday.
Help Sam determine the volume of the biggest piece of cake that resulted from these two cuts.

\includegraphics{cake.png}
Input
The input consists of a single line containing three integers n (2≤n≤10000), the length of the sides of the square cake in centimeters,
h (0<h<n), the distance of the horizontal cut from the top edge of the cake in centimeters, and v (0<v<n), 
the distance of the vertical cut from the left edge of the cake in centimeters. This is illustrated in the figure above.

Each cake is 4 centimeters thick.

Output
Display the volume (in cubic centimeters) of the largest of the four pieces of cake after the horizontal and vertical cuts are made."""



def volcake():
    x,y,z = map(int,input().split())
    l = int(x)
    v = int(y)
    h = int(z)
    if l - v > v:
        v = l - v
    if l - h > h:
      h = l - h
    return(v*h*4)


#def volkake():
   # x = input().split
   # a = int(x[0])
   # b = int(x[1])
   # c = int(x[2])
   # if a - b > b:
   #     b = a - b
   # if a - c > c:
   #     c = a - c
   # return a*b*4

print(volcake())


