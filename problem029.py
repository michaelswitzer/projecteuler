# Consider all integer combinations of a**b for 2 <= a <= 5 and 2 <= b <= 5:
# 
# 2**2=4, 2**3=8, 2**4=16, 2**5=32 3**2=9, 3**3=27, 3**4=81, 3**5=243 4**2=16, 4**3=64,
# 4**4=256, 4**5=1024 5**2=25, 5**3=125, 5**4=625, 5**5=3125 If they are then placed
# in numerical order, with any repeats removed, we get the following
# sequence of 15 distinct terms:
# 
# 4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125
# 
# How many distinct terms are in the sequence generated by ab for 2 <= a <= 100
# and 2 <= b <= 100?

import math
import itertools

# http://stackoverflow.com/questions/15347174/python-finding-prime-factors
def prime_factors(n):
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
    
    
    
def exponent_gen(a,b):
    exps = []
    pf_a = prime_factors(a)
    
    for x in pf_a:
        x_count = pf_a.count(x)
        exps.append([x, x_count * b])
        
    exps = list(exps for exps,_ in itertools.groupby(exps)) # use itertools to remove dupes: http://stackoverflow.com/questions/2213923/python-removing-duplicates-from-a-list-of-lists
    return exps
        
unique_terms = []
for a in range(2,101):
    for b in range(2,101):
        exps = exponent_gen(a,b)
        if exps not in unique_terms:
            unique_terms.append(exps)

print(len(unique_terms))
    