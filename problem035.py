# The number, 197, is called a circular prime because all rotations of the
# digits: 197, 971, and 719, are themselves prime.
# 
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31,
# 37, 71, 73, 79, and 97.
# 
# How many circular primes are there below one million?

from common_funcs import answer, is_prime

# returns all rotations of n
def rotations(n):
    rotate = []
    digits = [int(x) for x in list(str(n))]
    for x in range(0, len(digits)):
        rotate.append(int(''.join(map(str, digits)))) #convert digits to int
        temp = digits.pop()
        digits.insert(0,temp)
    return rotate
    
def all_rotations_prime(n):
    for x in rotations(n):
        if not is_prime(x):
            return False
    return True
 
def solve():   
    count = 1
    for x in range(3,1000000,2):
        if all_rotations_prime(x):
            count += 1
    return count
    
answer(solve)