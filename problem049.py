# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
# increases by 3330, is unusual in two ways: (i) each of the three terms
# are prime, and, (ii) each of the 4-digit numbers are permutations of one
# another.
# 
# There are no arithmetic sequences made up of three 1, 2, or 3digit
# primes, exhibiting this property, but there is one other 4-digit
# increasing sequence.
# 
# What 12-digit number do you form by concatenating the three terms in
# this sequence?

from common_funcs import answer, is_prime, is_permutation

def test_seq(n):
    for x in range(0,3):
        seq_term = guess + x * seq_len
        print(seq_term)
        if not is_permutation(seq_term, guess) and not is_prime(seq_term):
            print("hello")
            break
        elif x == 2:
            return int(str(guess) + str(guess + seq_len) + str(guess + 2 * seq_len))

def solve():
    for guess in range(1488,10000): # checked in testing that it's not before 1487
        for seq_len in range(1,9999):
            if guess + 2 * seq_len > 9999:
                break
            for x in range(0,3):
                seq_term = guess + x * seq_len
                if not is_permutation(seq_term, guess) or not is_prime(seq_term):
                    break
                elif x == 2:
                    return int(str(guess) + str(guess + seq_len) + str(guess + 2 * seq_len))

answer(solve)