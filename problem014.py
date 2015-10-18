# The following iterative sequence is defined for the set of positive
# integers:
# 
# n = n/2 (n is even) 
# n = 3n + 1 (n is odd)
# 
# Using the rule above and starting with 13, we generate the following
# sequence:
# 
# 13  40  20  10  5  16  8  4  2  1 It can be seen that this
# sequence (starting at 13 and finishing at 1) contains 10 terms. Although
# it has not been proved yet (Collatz Problem), it is thought that all
# starting numbers finish at 1.
# 
# Which starting number, under one million, produces the longest chain?
# 
# NOTE: Once the chain starts the terms are allowed to go above one
# million.

from common_funcs import answer

def is_even(n):
    if n % 2 == 0:
        return True
    return False

def seq_length(n):
    steps = 0
    while n != 1:
        if is_even(n):
            n = n / 2
        else:
            n = 3 * n + 1
        steps = steps + 1
    return steps

def solve():
    greatest = 0
    for n in range(1,1000000):
        seq_l = seq_length(n)
        if seq_l > greatest:
            greatest = seq_l
            greatest_n = n
    return greatest_n
    
answer(solve)