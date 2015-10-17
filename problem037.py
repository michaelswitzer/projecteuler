# The number 3797 has an interesting property. Being prime itself, it is
# possible to continuously remove digits from left to right, and remain
# prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
# right to left: 3797, 379, 37, and 3.
# 
# Find the sum of the only eleven primes that are both truncatable from
# left to right and right to left.
# 
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

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

truncatable_primes = []

guess = 10
while len(truncatable_primes) < 11:
    if truncatable(guess):
        truncatable_primes.append(guess)
        print(truncatable_primes)  
    guess += 1 
    
print(sum(truncatable_primes))

