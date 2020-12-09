
"""The factorial of N, written as N!, is defined as the product of all the integers from 1 to N. For example, 3!=1×2×3=6.

This number can be very large, so instead of computing the entire product, just compute the last digit of N! (when N! is written in base 10).

Input
The first line of input contains a positive integer 1≤T≤10, the number of test cases. Each of the next T lines contains a single positive 
integer N. N is at most 10.

Output
For each value of N, print the last digit of N!."""

#def fact(n):
   # if n < 0:
      #  print("Illegal to use negative integers.")
      #  n *= fact(n-1)
      #  return n
   # else:
       # return 1

#for x in range(int(input())):
   # print(fact(int(input)))%10


    #def LastFactorDigit(n):
        #if n != 0:
            #n *= LastFactorDigit(n-1)
            #return n
        #else:
            #return 1

#for i in range(int(input())):
    #print(LastFactorDigit(int(input()))%10)

def pos_neg(a, b, negative):
  if negative:
    if pos_negtwo(a, b):
      return True
    else:
      return False
  if pos_negthree(a, b):
    return True
  else:
    return False
  
  
def pos_negtwo(a, b):
  if a < 0 and b < 0: 
    return True
  else:
    return False

def pos_negthree(a, b):
  if a < 0 or b < 0:
    return True
  if pos_negtwo(a, b):
    return True
  else:
   return False

a = int(input())
b = int(input())
c = bool(input())

print(pos_neg(a, b, c))

