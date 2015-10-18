# The fraction 49/98 is a curious fraction, as an inexperienced
# mathematician in attempting to simplify it may incorrectly believe that
# 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
# 
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
# 
# There are exactly four non-trivial examples of this type of fraction,
# less than one in value, and containing two digits in the numerator and
# denominator.
# 
# If the product of these four fractions is given in its lowest common
# terms, find the value of the denominator.

import fractions

from common_funcs import answer

# tell if fraction is curious
# only supports 2 digits in num, den
def curious(n,d):
    # individual digits in num and den
    n = float(n)
    d = float(d)
    n_d1 = float(str(n)[0])
    n_d2 = float(str(n)[1])
    d_d1 = float(str(d)[0])
    d_d2 = float(str(d)[1])
    try:
        if ((n/d == n_d1/d_d2 and n_d2==d_d1) or (n/d == n_d2/d_d1 and n_d1 == d_d2)) and n_d1 != n_d2 and n/d < 1:
            return True
    except ZeroDivisionError:
        pass
    return False

def solve():   
    num_prod = 1
    den_prod = 1
    for num in range(10,100):
        for den in range(10,100):
            if curious(num,den):
                num_prod *= num
                den_prod *= den
            
    print "Unreduced fraction: ", num_prod, " / ", den_prod
    return fractions.Fraction(num_prod,den_prod).denominator

answer(solve)