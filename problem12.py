# The sequence of triangle numbers is generated by adding the natural
# numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 =
# 28. The first ten terms would be:
# 
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# 
# Let us list the factors of the first seven triangle numbers:
# 
#  1: 1 
#  3: 1,3 
#  6: 1,2,3,6 
#  10: 1,2,5,10 
#  15: 1,3,5,15 
#  21: 1,3,7,21 
#  28: 1,2,4,7,14,28
#  We can see that 28 is the first triangle number to have
#  over five divisors.
# 
# What is the value of the first triangle number to have over five hundred
# divisors?

#method 2: find primes and spaces within them and count triangle numbers

#filter triangle numbers

#method 1: check all nums

import time
import math

# O(1)
def triangleNum(n):
    Tn = (n * (n + 1)) / 2 # From Wikipedia
    return Tn

# from http://stackoverflow.com/questions/171765/what-is-the-best-way-to-get-all-the-divisors-of-a-number
# his comments make me feel better for looking this up. I promise I learned a lot.
def divisorGenerator(n):
    large_divisors = []
    for i in xrange(1, int(math.sqrt(n) + 1)):
        if n % i is 0:
            yield i
            if i is not n / i:
                large_divisors.insert(0, n / i)
    for divisor in large_divisors:
        yield divisor
    
n = 1
max = 500

start = time.time()

while(True):
    t = triangleNum(n)
    num_divisors = len(list(divisorGenerator(t)))

    print n, t, num_divisors
    
    if num_divisors > max:
        print "Speed: ", time.time() - start, "Seconds"
        break

    n = n + 1