# We shall say that an n-digit number is pandigital if it makes use of all
# the digits 1 to n exactly once. For example, 2143 is a 4-digit
# pandigital and is also prime.
# 
# What is the largest n-digit pandigital prime that exists?

from itertools import permutations

from common_funcs import answer, is_prime, is_pandigital


def solve():
    best_case = '987654321' # 9 digit pandigital would be ideal
    while best_case != '':
        guess_perms = sorted([int(''.join(p)) for p in permutations(best_case)], reverse = True) # find all pandigitals

        for guess in guess_perms:
            if is_pandigital(guess, len(best_case)) and is_prime(guess):
                return guess
            else:
                guess -= 1
            
        best_case = best_case[1:] # truncate if we give up on this many digits

answer(solve)