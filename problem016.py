# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# 
# What is the sum of the digits of the number 2^1000?

from common_funcs import answer, sum_digits

def solve():
    return sum_digits(2**1000)

answer(solve)