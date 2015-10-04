# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# 
# Find the sum of all the primes below two million.

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
    

def primes_below(n):
    total = 0
    for x in range(1,n):
        if is_prime(x):
            total = total + x
    return total

print("Primes below 10: ", primes_below(10))
print("Primes below 2000000: ", primes_below(2000000))
            