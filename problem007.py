# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
# see that the 6th prime is 13.
# 
# What is the 10 001st prime number?

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
    
    
counter = 1
nat = 1

while(counter < 10001):
    nat = nat + 2
    if is_prime(nat):
        print("Prime: ",nat)
        counter = counter + 1
