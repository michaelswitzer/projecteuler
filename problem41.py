# We shall say that an n-digit number is pandigital if it makes use of all
# the digits 1 to n exactly once. For example, 2143 is a 4-digit
# pandigital and is also prime.
# 
# What is the largest n-digit pandigital prime that exists?

from itertools import permutations

class We_Won(Exception): pass

def is_pandigital(n, length):
    digits = [int(x) for x in list(str(n))]
    for x in range(1,length+1):
        if x in digits:
            digits.remove(x)
        else:
            return False
    if digits == []:
        return True
        
#naive primality test from wikipedia
def is_prime(n):
    if n <= 1:
        return False
    elif n <=3:
        return True
    elif (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while i*i <= n:
        if (n % i == 0 or n % (i+2) == 0):
            return False
        i = i + 6
    return True

best_case = '987654321' # 9 digit pandigital would be ideal

try:
    while best_case != '':
        guess_perms = sorted([int(''.join(p)) for p in permutations(best_case)], reverse = True) # find all pandigitals

        for guess in guess_perms:
            if is_pandigital(guess, len(best_case)) and is_prime(guess):
                print guess
                raise We_Won
            else:
                guess -= 1
            
        best_case = best_case[1:] # truncate if we give up on this many digits
except We_Won:
    pass