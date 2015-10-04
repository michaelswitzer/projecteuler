#If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.

def multiples_below(below, m1, m2):
    total = 0
    for x in range(0,below):
        if(x % m1 == 0 or x % m2 == 0):
            total = total + x  
    return(total)
    
print(multiples_below(1000,3,5))