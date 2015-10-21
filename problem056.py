# A googol (10**100) is a massive number: one followed by one-hundred zeros;
# 100**100 is almost unimaginably large: one followed by two-hundred zeros.
# Despite their size, the sum of the digits in each number is only 1.
# 
# Considering natural numbers of the form, a**b, where a, b < 100, what is
# the maximum digital sum?

from common_funcs import answer, sum_digits

def solve():
    maximum = 0
    for a in range(1,100):
        for b in range(1,100):
            digi_sum = sum_digits(a**b)
            if digi_sum > maximum:
                maximum = digi_sum
    return maximum
    
answer(solve)