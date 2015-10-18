# A Pythagorean triplet is a set of three natural numbers, a < b < c, for
# which,
# 
# a**2 + b**2 = c**2 For example, 32 + 42 = 9 + 16 = 25 = 5**2.
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

from common_funcs import answer

def find_abc(sum):
    for a in range(1,sum): #ugh
        for b in range(a+1,sum): #ughhh
            for c in range(b+1,sum): #UGH
                if (a + b + c == 1000 and a**2 + b**2 == c**2):
                    return a*b*c
                    
def solve():
    return find_abc(1000)
                    
answer(solve)