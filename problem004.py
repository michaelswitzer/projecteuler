# A palindromic number reads the same both ways. The largest palindrome
# made from the product of two 2-digit numbers is 9009 = 91 * 99.
# 
# Find the largest palindrome made from the product of two 3-digit numbers.

from common_funcs import answer, is_palindrome

def solve():
    largest = 0
    for i in range(999,100,-1):
        for j in range(i,100,-1):
            if(is_palindrome(i*j) and i*j > largest):
                largest = i*j
    return largest

answer(solve)