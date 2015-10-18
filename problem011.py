# In the 20*20 grid below, four numbers along a diagonal line have been
# marked in red.
# 
# <<<grid below>>>
# 
# The product of these numbers is 26 * 63 * 78 * 14 = 1788696.
# 
# What is the greatest product of four adjacent numbers in the same
# direction (up, down, left, right, or diagonally) in the 20*20 grid?

from common_funcs import answer
from data_sets import problem011_data

grid = problem011_data()
        
def search_right(matrix, i, j):
    try:
        return matrix[i][j] * matrix[i][j+1] * matrix[i][j+2] * matrix[i][j+3]
    except IndexError:
        return 0
        
def search_down(matrix, i, j):
    try:
        return matrix[i][j] * matrix[i+1][j] * matrix[i+2][j] * matrix[i+3][j]
    except IndexError:
        return 0
        
def search_diagup(matrix, i, j):
    try:
        return matrix[i][j] * matrix[i+1][j+1] * matrix[i+2][j+2] * matrix[i+3][j+3]
    except IndexError:
        return 0

def search_diagdown(matrix, i, j):
    try:
        return matrix[i][j] * matrix[i-1][j+1] * matrix[i-2][j+2] * matrix[i-3][j+3]
    except IndexError:
        return 0


def greatest_prod(matrix):
    greatest = 0
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[i])):
            searches = [search_right(matrix,i,j), search_down(matrix,i,j), search_diagup(matrix,i,j), search_diagdown(matrix,i,j)]
            if max(searches) > greatest:
                greatest = max(searches)
    return greatest
            
def solve():
    return greatest_prod(grid)
            
answer(solve)