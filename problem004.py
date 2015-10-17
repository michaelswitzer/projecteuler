# A palindromic number reads the same both ways. The largest palindrome
# made from the product of two 2-digit numbers is 9009 = 91 * 99.
# 
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(n):
    n_str = str(n)
    n_len = len(n_str)
    for x in range(0, n_len/2):
        if(n_str[x] != n_str[-1 - x]):
            return False
    return True
    
print("is 123 a palindrome: ", is_palindrome(123))
print("is 313 a palindrome: ", is_palindrome(313))

# solve problem

largest = 0

for i in range(999,100,-1):
    for j in range(999,100,-1):
        if(is_palindrome(i*j) and i*j > largest):
            largest = i*j
            print(largest)