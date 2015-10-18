# By starting at the top of the triangle below and moving to adjacent
# numbers on the row below, the maximum total from top to bottom is 23.
# 
# 3
# 7 4
# 2 4 6
# 8 5 9 3
# 
# That is, 3 + 7 + 4 + 9 = 23.
# 
# Find the maximum total from top to bottom of the triangle below:

# NOTE: As there are only 16384 routes, it is possible to solve this
# problem by trying every route. However, Problem 67, is the same
# challenge with a triangle containing one-hundred rows; it cannot be
# solved by brute force, and requires a clever method! ;o)

from common_funcs import answer
from data_sets import problem018_data

def max_total(tri):
    for x in range(0,len(tri)-1):
        next = tri.pop()
        for y in range(0,len(next)-1):
            if next[y] > next[y+1]:
                tri[-1][y] = tri[-1][y] + next[y]
            else:
                tri[-1][y] = tri[-1][y] + next[y+1]
    return tri[0][0]
    
def solve():
    triangle = problem018_data()
    return max_total(triangle)
                
answer(solve)