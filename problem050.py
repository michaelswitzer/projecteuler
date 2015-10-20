# The prime 41, can be written as the sum of six consecutive primes:
# 
# 41 = 2 + 3 + 5 + 7 + 11 + 13 
# This is the longest sum of consecutive
# primes that adds to a prime below one-hundred.
# 
# The longest sum of consecutive primes below one-thousand that adds to a
# prime, contains 21 terms, and is equal to 953.
# 
# Which prime, below one-million, can be written as the sum of the most
# consecutive primes?

from common_funcs import answer, primes_less_than

# http://www.geeksforgeeks.org/largest-sum-contiguous-subarray/ 
# was interesting, but ultimately unhelpful. I don't know if there is a
# way to reliably generate sums of primes that are prime, so I am brute
# forcing it by checking all contiguous sums.

def solve():
    primes = primes_less_than(1000000) # returns List
    primes_set = set(primes) # doing this for faster search later

    best_counter = 0
    best_total = 0
    
    for n in primes:
        total = n
        counter = 1
        for p in primes[primes.index(n)+1:]:
            total += p
            counter += 1
            if total >= 1000000:
                counter = 0
                break
            if total in primes_set and counter > best_counter:
                best_counter = counter
                best_total = total
    
    return best_total

        
answer(solve)