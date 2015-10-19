# The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.
# 
# Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.

from common_funcs import answer

def solve():
    total = 0
    for x in range(1,1001):
        if 1 <= x <= 10:
            total += int(str(x**x)[-x:])
        else:   
            total += int(str(x**x)[-10:])
            
    return int(str(total)[-10:])
    
    
answer(solve)