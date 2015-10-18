# Using names.txt (right click and 'Save Link/Target As...'), a 46K text
# file containing over five-thousand first names, begin by sorting it into
# alphabetical order. Then working out the alphabetical value for each
# name, multiply this value by its alphabetical position in the list to
# obtain a name score.
# 
# For example, when the list is sorted into alphabetical order, COLIN,
# which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
# So, COLIN would obtain a score of 938 * 53 = 49714.
# 
# What is the total of all the name scores in the file?

import string

from common_funcs import answer
from data_sets import problem022_data

def solve():
    names = problem022_data()

    sorted_names = sorted(names)

    # http://stackoverflow.com/questions/3246262/python-how-do-i-assign-values-to-letters
    values = dict()
    for index, letter in enumerate(string.ascii_uppercase):
       values[letter] = index + 1

    totalscore = 0

    for whichname in range(0,len(names)):
        name_score = 0
        for pos in sorted_names[whichname]:
            name_score = name_score + values[pos]
        name_score = name_score * (whichname+1)
        totalscore = totalscore + name_score
    return totalscore

answer(solve)