# Surprisingly there are only three numbers that can be written as the sum
# of fourth powers of their digits:
# 
# 1634 = 1**4 + 6**4 + 3**4 + 4**4
# 8208 = 8**4 + 2**4 + 0**4 + 8**4
# 9474 = 9**4 + 4**4 + 7**4 + 4**4
# As 1 = 1**4 is not a sum it is not included.
# 
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
# 
# Find the sum of all the numbers that can be written as the sum of fifth
# powers of their digits.

# checks if sum of digits of p to the power of n are equal to p
def digitChecker(p,n):
    list_digits = [int(x) for x in list(str(p))]
    total = 0
    for x in list_digits:
        total += x**n
    if total == p:
        return True
    else:
        return False

total = 0
check = 11

# this is incredibly lazy; I assume there's a proof that shows the
# maximum number. I am just banking on brute force being computationally
# feasible.
while True:
    if digitChecker(check,5):
        print(check)
        total += check
        print(total)
    check += 1