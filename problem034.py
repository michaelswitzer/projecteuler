# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# 
# Find the sum of all numbers which are equal to the sum of the factorial
# of their digits.
# 
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

import math
import time

from common_funcs import answer

def solve():
    begin_time = time.time()

    guess = 3

    answer_sum = 0

    while time.time() - begin_time < 1: #laaazy
        digits = [int(x) for x in list(str(guess))]
        sum = 0
        for x in digits:
            sum += math.factorial(x)
        if guess == sum:
            answer_sum += guess
        guess+= 1
    
    return answer_sum
    
answer(solve)