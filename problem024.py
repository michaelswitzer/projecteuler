# A permutation is an ordered arrangement of objects. For example, 3124
# is one possible permutation of the digits 1, 2, 3 and 4. If all of the
# permutations are listed numerically or alphabetically, we call it
# lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
# 
# 012   021   102   120   201   210
# 
# What is the millionth lexicographic permutation of the digits 0, 1, 2,
# 3, 4, 5, 6, 7, 8 and 9?
# 

import string

from common_funcs import answer

# https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order 
def iterate_lex(a):
    index1 = []
    index2 = []
    
    # Find the largest index k such that a[k] < a[k + 1].
    for k in range(0,len(a)):
        try:
            if a[k] < a[k+1]:
                index1.append(k)
        except IndexError:
            pass
    index1 = max(index1)
    
    # Find the largest index l greater than k such that a[k] < a[l]
    for l in range(0,len(a)):
        if a[l] > a[index1]:
            index2.append(l)
    index2 = max(index2)
    
    #switcheroo
    a[index1], a[index2] = a[index2], a[index1]
    
    #Reverse the sequence from a[k + 1] up to and including the final element a[n].
    a[index1+1:] = reversed(a[index1+1:])
        
    return a

def solve():
    digits_list = [int(x) for x in list(string.digits)]

    for _ in range(999999):
        digits_list = iterate_lex(digits_list)

    ans = 0
    for x in range(10):
        ans = ans + (10**(9-x))*digits_list[x]
    return ans
        
answer(solve)