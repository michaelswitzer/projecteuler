# Starting with the number 1 and moving to the right in a clockwise
# direction a 5 by 5 spiral is formed as follows:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
# 
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
# formed in the same way?

# 1 2 2 2 2 4 4 4 4 6 6 6 6

from common_funcs import answer

# for spiral of size n, return sum of diagonals
# for the problem it will be spiralSum(1001**2)
def spiralSum(n):

    sum = 0
    increment = 2
    counter = 0
    diag_dist = 2
    
    for i in range(0,n):
        if i % diag_dist == 0:
            sum = sum + 1 + i
            counter += 1
        if counter == 4:
            diag_dist = diag_dist + increment
            counter = 0

    return sum
    
def solve():
    return spiralSum(1001**2)

answer(solve)