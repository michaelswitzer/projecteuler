# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# 
# What is the sum of the digits of the number 2^1000?

import math

# wikipedia for digit sum: 
# digit sum of 2**1000 is sum from n=0 to log(2**1000) of
#  (1/10**n)*(((2**1000) % 10**(n+1)) - ((2**1000) % 10**n)

max = int(math.floor(1000 * math.log10(2)))

total = 0
for n in range(max+1):
    total = total + (((2**1000) % 10**(n+1)) - ((2**1000) % 10**n)) / (10**n)
print "answer:", total