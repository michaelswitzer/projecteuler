# There are exactly ten ways of selecting three from five, 12345:
# 
# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
# 
# In combinatorics, we use the notation, 5 C 3 = 10.
# 
# In general,
# 
# nCr =	n! / r!(n-r)!
# 
# where r <= n, n! = n*(n-1)*...*3*2*1, and 0! = 1. It is not until n =
# 23, that a value exceeds one-million: 23 C 10 = 1144066.
# 
# How many, not necessarily distinct, values of  nCr, for 1 <= n <= 100,
# are greater than one-million?

from common_funcs import answer
from math import factorial

def C(n,r):
    return factorial(n) / (factorial(r) * factorial(n-r))

def solve():
    counter = 0
    for n in range(23,101):
        for r in range(1,n+1):
            if C(n,r) > 1000000:
                counter += 1
    return counter
     
answer(solve)