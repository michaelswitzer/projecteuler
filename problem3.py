# The prime factors of 13195 are 5, 7, 13 and 29.
# 
# What is the largest prime factor of the number 600851475143 ?

import math

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


def prime_factorize(n):
    prime_factors = []
    for x in range(1,int(math.sqrt(n))):
        if (n % x == 0 and is_prime(x)):
            prime_factors.append(x)
            x = 1
            n = n / x
    return prime_factors
            
# solve problem
num = 600851475143 
print(prime_factorize(num))