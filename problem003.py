# The prime factors of 13195 are 5, 7, 13 and 29.
# 
# What is the largest prime factor of the number 600851475143 ?

from common_funcs import answer, prime_factors

def solve():
    num = 600851475143
    return max(prime_factors(num))

answer(solve)