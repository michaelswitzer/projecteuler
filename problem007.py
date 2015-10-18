# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
# see that the 6th prime is 13.
# 
# What is the 10 001st prime number?

from common_funcs import answer, is_prime
      
def solve():
    counter = 1
    nat = 1

    while(counter < 10001):
        nat = nat + 2
        if is_prime(nat):
            counter = counter + 1
    return nat

answer(solve)