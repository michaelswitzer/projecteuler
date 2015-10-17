# We shall say that an n-digit number is pandigital if it makes use of all
# the digits 1 to n exactly once; for example, the 5-digit number, 15234,
# is 1 through 5 pandigital.
# 
# The product 7254 is unusual, as the identity, 39 * 186 = 7254,
# containing multiplicand, multiplier, and product is 1 through 9
# pandigital.
# 
# Find the sum of all products whose multiplicand/multiplier/product
# identity can be written as a 1 through 9 pandigital.
# 
# HINT: Some products can be obtained in more than one way so be sure to
# only include it once in your sum.

def product_pandigital(a,b):
    c = a * b
    digits = [int(x) for x in list(str(a)) + list(str(b)) + list(str(c))]
    for x in range(1,10):
        if x in digits:
            digits.remove(x)
        else:
            return False
    if digits == []:
        return True
    return False
    
# tests
print(product_pandigital(39,186))
print(product_pandigital(39,187))

products = []
for a in range(1,500): #total guess
    for b in range(1,5000):
        if product_pandigital(a,b) and a*b not in products:
            products.append(a*b)

print(sum(products))