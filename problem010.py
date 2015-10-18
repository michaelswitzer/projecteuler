# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# 
# Find the sum of all the primes below two million.

from common_funcs import answer, is_prime  

def primes_below(n):
    total = 2 
    for x in xrange(3,n,2):
        if is_prime(x):
            total = total + x
    return total
    
def solve():
    return primes_below(2000000)

answer(solve)