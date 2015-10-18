# The number 3797 has an interesting property. Being prime itself, it is
# possible to continuously remove digits from left to right, and remain
# prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
# right to left: 3797, 379, 37, and 3.
# 
# Find the sum of the only eleven primes that are both truncatable from
# left to right and right to left.
# 
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

from common_funcs import answer, is_prime
    
def truncatable(n):
    left = str(n)
    right = str(n)
    while left != '':
        if not is_prime(int(left)):
            return False
        left = left[1:]
    while right != '':
        if not is_prime(int(right)):
            return False
        right = right[:-1]
    return True

def solve():
    truncatable_primes = []

    guess = 10
    while len(truncatable_primes) < 11:
        if truncatable(guess):
            truncatable_primes.append(guess) 
        guess += 1 
    
    return sum(truncatable_primes)
    
answer(solve)

