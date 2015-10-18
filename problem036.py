# The decimal number, 585 = 1001001001 (binary), is palindromic in both
# bases.
# 
# Find the sum of all numbers, less than one million, which are
# palindromic in base 10 and base 2.
# 
# (Please note that the palindromic number, in either base, may not
# include leading zeros.)

from common_funcs import answer, is_palindrome
  
def solve():    
    total = 0
    for x in range(1,1000000):
        if is_palindrome(x) and is_palindrome(str(bin(x))[2:]):
            total += x
    return total

answer(solve)