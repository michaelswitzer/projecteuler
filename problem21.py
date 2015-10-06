# Let d(n) be defined as the sum of proper divisors of n (numbers less
# than n which divide evenly into n). If d(a) = b and d(b) = a, where a !=
# b, then a and b are an amicable pair and each of a and b are called
# amicable numbers.
# 
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22,
# 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are
# 1, 2, 4, 71 and 142; so d(284) = 220.
# 
# Evaluate the sum of all the amicable numbers under 10000.

import math

# from http://stackoverflow.com/questions/171765/what-is-the-best-way-to-get-all-the-divisors-of-a-number
def divisorGenerator(n):
    large_divisors = []
    for i in xrange(1, int(math.sqrt(n) + 1)):
        if n % i is 0:
            yield i
            if i is not n / i:
                large_divisors.insert(0, n / i)
    for divisor in large_divisors[:-1]: # modified to not include number itself as a divisor
        yield divisor
        
def d(n):
    return sum(list(divisorGenerator(n)))
    
# generate all amicable nums under n
def amicableGenerator(n):
    ami = [] 
    for a in range(1, n):
        b = d(a) # d(a)
        db = d(b) # a
        if a != b and db == a: 
            ami.append(a)
            ami.append(b)
    return list(set(ami)) # remove duplicates
    
print(sum(amicableGenerator(10000)))