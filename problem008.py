# The four adjacent digits in the 1000-digit number that have the greatest
# product are 9 * 9 * 8 * 9 = 5832.
# 
# <<<INSERT BIG NUMBER HERE!!!!>>>
# 
# Find the thirteen adjacent digits in the 1000-digit number that have the
# greatest product. What is the value of this product?

from common_funcs import answer
from data_sets import problem008_data

def solve():
    big_num = problem008_data()

    most = 0

    for x in range(0,1000-13):
        prod = 1
        for y in range(13):
            prod = prod * int(big_num[x+y])
        if(prod > most):
            most = prod
    return most
        
answer(solve)