# The Fibonacci sequence is defined by the recurrence relation:
# 
# Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
# 
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.
# 
# What is the index of the first term in the Fibonacci sequence to contain
# 1000 digits?

from math import sqrt, log10
   
# http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibFormula.html#logs 
phi = (1 + 5 ** 0.5) / 2

# number of digits in fib number n
def fib_digits(n):
    return n*log10(phi) - log10(5) / 2    

index = 1
while round(fib_digits(index)) < 1001:
    index = index + 1
print fib_digits(index), index