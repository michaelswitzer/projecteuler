# It was proposed by Christian Goldbach that every odd composite number
# can be written as the sum of a prime and twice a square.
# 
# 9 = 7 + 2*1^2
# 15 = 7 + 2*2^2
# 21 = 3 + 2*3^2
# 25 = 7 + 2*3^2
# 27 = 19 + 2*2^2
# 33 = 31 + 2*1^2
# 
# It turns out that the conjecture was false.
# 
# What is the smallest odd composite that cannot be written as the sum of
# a prime and twice a square?

from common_funcs import answer, is_prime

def sum_prime_twice_square(guess, primes):
    for prime in primes:
        coef = 1
        while True:
            tester = prime + 2 * coef**2
            if tester == guess:
                return True
            elif tester > guess:
                break
            coef += 1
    return False

def solve():
    primes = [2]
    guess = 3
    while True:
        if is_prime(guess):
            primes.append(guess)
        elif not sum_prime_twice_square(guess, primes):
            return guess
        guess += 2

answer(solve)