# The number, 197, is called a circular prime because all rotations of the
# digits: 197, 971, and 719, are themselves prime.
# 
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31,
# 37, 71, 73, 79, and 97.
# 
# How many circular primes are there below one million?

# returns all rotations of n
def rotations(n):
    rotate = []
    digits = [int(x) for x in list(str(n))]
    for x in range(0, len(digits)):
        rotate.append(int(''.join(map(str, digits)))) #convert digits to int
        temp = digits.pop()
        digits.insert(0,temp)
    return rotate
    
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
    
def all_rotations_prime(n):
    for x in rotations(n):
        if not is_prime(x):
            return False
    return True
    
count = 0
for x in range(2,1000000):
    if all_rotations_prime(x):
        count += 1
    
print(count)