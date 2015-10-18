# The nth term of the sequence of triangle numbers is given by, tn =
# .5n(n+1); so the first ten triangle numbers are:
# 
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# 
# By converting each letter in a word to a number corresponding to its
# alphabetical position and adding these values we form a word value. For
# example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word
# value is a triangle number then we shall call the word a triangle word.
# 
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text
# file containing nearly two-thousand common English words, how many are
# triangle words?

from common_funcs import answer
from data_sets import problem042_data

words = problem042_data()

def letter_value(s):
    return ord(s)-64

def word_value(s):
    value = 0
    for letter in s:
        value += letter_value(letter)
    return value
    
def is_triangle_word(s): # inefficient but i know i can brute force this
    value = word_value(s)
    triangle_num = 1
    n = 0
    while triangle_num <= value:
        n += 1
        triangle_num = n * (n + 1) / 2
        if value == triangle_num:
            return True
    return False
   
def solve(): 
    how_many = 0
    for word in words:
        if is_triangle_word(word):
            how_many += 1
    return how_many
        
answer(solve)