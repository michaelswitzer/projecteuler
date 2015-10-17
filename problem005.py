# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
# 
# What is the smallest positive number that is evenly divisible by all of
# the numbers from 1 to 20?

def evenly_divisible(nat,up_to):
    for x in range(1,up_to):
        if (nat % x != 0):
            return False
    return True


# solve problem
smallest = 20 #starting guess
while(True): #yeah pretty sure this is the worlds worst idea thanks
    print(smallest)
    if evenly_divisible(smallest,20):
        break
    smallest = smallest + 20 #has to be divisible by 20 so this is my increment