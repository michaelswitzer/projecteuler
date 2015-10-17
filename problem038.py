# Take the number 192 and multiply it by each of 1, 2, and 3:
# 
# 192 * 1 = 192
# 192 * 2 = 384
# 192 * 3 = 576
#
# By concatenating each product we get the 1 to 9 pandigital, 192384576.
# We will call 192384576 the concatenated product of 192 and (1,2,3)
# 
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3,
# 4, and 5, giving the pandigital, 918273645, which is the concatenated
# product of 9 and (1,2,3,4,5).
# 
# What is the largest 1 to 9 pandigital 9-digit number that can be formed
# as the concatenated product of an integer with (1,2, ... , n) where n >
# 1?

class We_Won(Exception): pass

def is_pandigital(n):
    digits = [int(x) for x in list(str(n))]
    for x in range(1,10):
        if x in digits:
            digits.remove(x)
        else:
            return False
    if digits == []:
        return True
        
guess = 50000 #definite maximum

try:
    while True:
        check_this = int(str(guess) + str(2*guess)) # base case
        n = 3
        while check_this <= 987654321:
            if is_pandigital(check_this):
                print "answer: ",check_this
                raise We_Won
            check_this = int(str(check_this) + str(n*guess))
            n += 1
        guess -= 1
except We_Won:
    pass