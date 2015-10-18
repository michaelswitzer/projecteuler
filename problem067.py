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
# Find the maximum total from top to bottom in triangle.txt (right click
# and 'Save Link/Target As...'), a 15K text file containing a triangle
# with one-hundred rows.
# 
# NOTE: This is a much more difficult version of Problem 18. It is not
# possible to try every route to solve this problem, as there are 299
# altogether! If you could check one trillion (1012) routes every second
# it would take over twenty billion years to check them all. There is an
# efficient algorithm to solve it. ;o)

from common_funcs import answer
from data_sets import problem067_data

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
    triangle = problem067_data()
    return max_total(triangle)
                
answer(solve)