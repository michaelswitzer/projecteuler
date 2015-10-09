# A unit fraction contains 1 in the numerator. The decimal representation
# of the unit fractions with denominators 2 to 10 are given:
# 
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# 
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It
# can be seen that 1/7 has a 6-digit recurring cycle.
# 
# Find the value of d < 1000 for which 1/d contains the longest recurring
# cycle in its decimal fraction part.

from decimal import *
from collections import Counter

def unitFraction(n):
    return str(Decimal(1) / Decimal(n))
    
# returns remainders appended together, aka long division
# http://stackoverflow.com/questions/29424349/implementing-long-division-using-a-generator-function-in-python
def decimals(n, d, length):
    while length > 0 and n % d != 0:
        n = n % d * 10
        yield n // d
        length -= 1
     
def findCycle(n, d):
    listLength = 10000 # experiment with different values
    a = list(decimals(n,d,listLength))
    
    for i in range(0,len(a)):
        for j in range(i+1,len(a)):
            if a[i:j] == a[j:j+len(a[i:j])] and a[i:j] == a[j+len(a[i:j]):j+2*len(a[i:j])]: #really messy but this means repeated 3 times
                return a[i:j]
    return []
    
# give example
for x in range(2,10):
    a = findCycle(1,x)
    print x, a    

# solve problem
biggest = []
for x in range(2,1000):
    a = findCycle(1,x)
    if len(biggest) < len(a):
        biggest = a
        print x
print x, biggest
        
    