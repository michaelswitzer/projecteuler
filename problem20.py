# n! means n * (n - 1) * ... * 3 * 2 * 1
# 
# For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800, and the sum of
# the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# 
# Find the sum of the digits in the number 100!

import math

# from wikipedia https://en.wikipedia.org/wiki/Digit_sum

num = math.factorial(100)

def sum_digits(num):
    total = 0
    max = int(math.floor(math.log10(num)))
    for n in range(0,max+1):
        total = total + (((num) % 10**(n+1)) - ((num) % 10**n)) / (10**n)
    return total

print(sum_digits(num))