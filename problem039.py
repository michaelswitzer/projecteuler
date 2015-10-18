# If p is the perimeter of a right angle triangle with integral length
# sides, {a,b,c}, there are exactly three solutions for p = 120.
# 
# {20,48,52}, {24,45,51}, {30,40,50}
# 
# For which value of p <= 1000, is the number of solutions maximised?

import math

from common_funcs import answer

def solve():
    most_solutions = 0

    for p in range(1,1001):
        solutions = []
        for a in range(3,p):
            for b in range(a+1,p):
                if math.sqrt(a**2 + b**2) == float(p - a - b):
                    solutions.append([a,b,p-a-b])
        if len(solutions) > most_solutions:
            most_solutions = len(solutions)
            best_p = p
    return best_p
        
answer(solve)