# An irrational decimal fraction is created by concatenating the positive
# integers:
# 
# 0.123456789101112131415161718192021...
# 
# It can be seen that the 12th digit of the fractional part is 1.
# 
# If dn represents the nth digit of the fractional part, find the value of
# the following expression.
# 
# d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000

from common_funcs import answer

def solve():
    decimals = "1"

    for x in range(2,200000):
        decimals = decimals + str(x)
    
    return int(decimals[0]) * int(decimals[9]) * int(decimals[99]) * int(decimals[999]) * int(decimals[9999]) * int(decimals[99999]) * int(decimals[999999])
    
answer(solve)