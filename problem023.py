# A perfect number is a number for which the sum of its proper divisors is
# exactly equal to the number. For example, the sum of the proper divisors
# of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
# number.
# 
# A number n is called deficient if the sum of its proper divisors is less
# than n and it is called abundant if this sum exceeds n.
# 
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
# smallest number that can be written as the sum of two abundant numbers
# is 24. By mathematical analysis, it can be shown that all integers
# greater than 28123 can be written as the sum of two abundant numbers.
# However, this upper limit cannot be reduced any further by analysis even
# though it is known that the greatest number that cannot be expressed as
# the sum of two abundant numbers is less than this limit.
# 
# Find the sum of all the positive integers which cannot be written as the
# sum of two abundant numbers.

from common_funcs import answer, div_gen

def isAbundant(n):
    if sum(list(div_gen(n))[:-1]) > n:
        return True
    return False
    
# returns array of abundant numbers between a and b
def abundantGenerator(a,b):
    abundants = []
    for x in range(a,b):
        if isAbundant(x):
            abundants.append(x)
    return abundants

# tests if n is a sum of two numbers in a list
def sumOfTwo(n, listOfNums):
    for x in list:
        for y in listOfNums:
            if x + y > n:
                break
            if x + y == n:
                return True
    return False
    
# generates all possible sums of two into a new list
def SumOfTwoGenerator(listOfNums):
    sumsOfTwo = []
    for x in listOfNums:
        for y in listOfNums:
            sumsOfTwo.append(x+y)
    return sorted(list(set(sumsOfTwo)))
      
    
def solve():  
    print("Generating abundants...") 
    abundants = abundantGenerator(12,28123)

    print("Generating possible sums...")
    Sums = SumOfTwoGenerator(abundants)

    print("Calculating answer...")
    total = 0
    for x in range(1,28123):
        if x not in Sums:
            total = total + x
    return total

answer(solve)