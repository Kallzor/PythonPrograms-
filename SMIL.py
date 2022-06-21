def SMIL():
    x = list(input())
    x.append("1")
    for i in range(len(x)):
        if x[i] == ":":
            if x[i+1] == ")":
                print(i)
            elif x[i+1] == "-":
                if x[i+2] == ")":
                    print(i)
        elif x[i] == ";":
            if x[i+1] == "-":
                if x[i+2] == ")":
                    print(i)


SMIL()
'''this is a joke of a program and this 
should be burned to the fucking ground and never be seen again by human eyes.
As someone who has done a bunch of kattis problems that are similar to this one before
with atleast 10x the efficency I am so fucking sad this is written by me.

But as a great progammer once said. If it works, it works. And this code BARELY fucking works and the solution
I have to the index out of range problem is so fucking dumb and cringe it's crazy
literally it's like trying to fix the falling of the twin towers with like some dutchtape.

Fuck this is so bad. I hope no-one ever looks at this solution'''

