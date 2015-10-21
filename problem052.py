# It can be seen that the number, 125874, and its double, 251748, contain
# exactly the same digits, but in a different order.
# 
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
# contain the same digits.

from common_funcs import answer, is_permutation

def x2_x3_x4_x5_x6_same_digits(x):
    x2 = 2*x
    x3 = 3*x
    x4 = 4*x
    x5 = 5*x
    x6 = 6*x
    if is_permutation(x2,x3) and is_permutation(x3,x4) and is_permutation(x4,x5) and is_permutation(x5,x6):
        return True
    else:
        return False
        
def solve():
    guess = 1
    while True:
        guess += 1
        if x2_x3_x4_x5_x6_same_digits(guess):
            return guess

answer(solve)