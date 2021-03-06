# The sum of the squares of the first ten natural numbers is,
# 
# 1^2 + 2^2 + ... + 10^2 = 385 The square of the sum of the first ten natural
# numbers is,
# 
# (1 + 2 + ... + 10)2 = 552 = 3025 Hence the difference between the sum of
# the squares of the first ten natural numbers and the square of the sum
# is 3025 - 385 = 2640.
# 
# Find the difference between the sum of the squares of the first one
# hundred natural numbers and the square of the sum.

from common_funcs import answer

def sum_squares(n):
    ans = 0
    for x in range(1,n+1):
        ans = ans + x**2
    return ans
        

def squared_sum(n):
    ans = 0
    for x in range(1,n+1):
        ans = ans + x
    return ans**2
    
def solve():
    interested_in = 100

    diff = squared_sum(interested_in) - sum_squares(interested_in)
    return diff
    
answer(solve)