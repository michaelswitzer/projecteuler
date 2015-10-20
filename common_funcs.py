# Common functions :
# Anything I've had to use more than once goes here

import math
import time
from itertools import permutations

### RETURNING AN ANSWER ###

def answer(method):
    start = time.time()
    result = method()
    end = time.time() - start

    print "Answer: %d" % result
    print "Speed: %0.6f seconds" % end

### PRIMES ###

# https://en.wikipedia.org/wiki/Primality_test#Pseudocode
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

    
# http://stackoverflow.com/questions/15347174/python-finding-prime-factors
def prime_expansion(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
    
def prime_factors(n):
    return list(set(prime_expansion(n)))
    
def primes_less_than(n):
    primes = []
    for i in range(2,n):
        if is_prime(i):
            primes.append(i)
    return primes
    

### PALINDROMES ###

def is_palindrome(n):
    n_str = str(n)
    n_len = len(n_str)
    for x in range(0, n_len/2):
        if(n_str[x] != n_str[-1 - x]):
            return False
    return True
    
    
### TRIANGLE NUMS ###
 
def triangle(n):
    return (n * (n + 1)) / 2
    
def triangular(Tn):
    # Tn inverse for positive n = (-1 + sqrt(8 * Tn + 1)) / 2
    Tn = float(Tn)
    if (-1 + math.sqrt(8 * Tn + 1) / 2).is_integer():
        return True
    return False

### PENTAGON NUMS ###

def pentagon(n):
    return n*(3*n-1)/2
    
def pentagonal(Pn):
    # Pn inverse = (sqrt(24 * Pn + 1) + 1) / 6
    Pn = float(Pn)
    if ((math.sqrt(24 * Pn + 1) + 1) / 6).is_integer():
        return True
    return False
    

### HEXAGON NUMS ###

def hexagon(n):
    return n*(2*n-1)
    
def hexagonal(Hn):
    # Hn inverse for positive n = (1 + sqrt(8 * Hn + 1)) / 4
    Hn = float(Hn)
    if ((1 + math.sqrt(8 * Hn + 1)) / 4).is_integer():
        return True
    return False
    
    
### DIVISORS ###

# http://stackoverflow.com/questions/171765/what-is-the-best-way-to-get-all-the-divisors-of-a-number
def div_gen(n):
    large_divisors = []
    for i in xrange(1, int(math.sqrt(n) + 1)):
        if n % i is 0:
            yield i
            if i is not n / i:
                large_divisors.insert(0, n / i)
    for divisor in large_divisors:
        yield divisor
        
### PERMUTATIONS ###

# http://stackoverflow.com/questions/104420/how-to-generate-all-permutations-of-a-list-in-python
def list_perms(n):
    return [int(''.join(p)) for p in permutations(n)]
    
# is n a permutation of p?
def is_permutation(n,p):
    n_list = sorted(list(str(n)))
    p_list = sorted(list(str(p)))
    if n_list == p_list:
        return True
    else:
        return False
        
### DIGIT MANIPULATION ###

# https://en.wikipedia.org/wiki/Digit_sum
def sum_digits(num):
    total = 0
    max = int(math.floor(math.log10(num)))
    for n in range(0,max+1):
        total = total + (((num) % 10**(n+1)) - ((num) % 10**n)) / (10**n)
    return total
    
### PANDIGITALS ###
        
def is_pandigital(n, length):
    digits = [int(x) for x in list(str(n))]
    for x in range(1,length+1):
        if x in digits:
            digits.remove(x)
        else:
            return False
    if digits == []:
        return True
        
        