# The first two consecutive numbers to have two distinct prime factors are:
# 
# 14 = 2 * 7
# 15 = 3 * 5
# 
# The first three consecutive numbers to have three distinct prime factors
# are:
# 
# 644 = 2**2 * 7 * 23
# 645 = 3 * 5 * 43
# 646 = 2 * 17 * 19.
# 
# Find the first four consecutive integers to have four distinct prime
# factors. What is the first of these numbers?

from common_funcs import answer, prime_factors

def solve():
    guess = 2
    count = 0
    while True:
        if len(prime_factors(guess)) == 4:
            count += 1
        else:
            count = 0
        if count == 4:
            return guess-3   
        guess += 1
        
answer(solve)