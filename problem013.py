# Work out the first ten digits of the sum of the following one-hundred
# 50-digit numbers.
# 
from common_funcs import answer
from data_sets import problem013_data

nums = problem013_data()

def solve():
    j = 10
    # add it all, convert answer to string and truncate. this seemed trivial
    return int(str(sum(nums))[:j])
    
answer(solve)

