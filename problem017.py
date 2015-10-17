# If the numbers 1 to 5 are written out in words: one, two, three, four,
# five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# 
# If all the numbers from 1 to 1000 (one thousand) inclusive were
# written out in words, how many letters would be used?
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred
# and forty-two) contains 23 letters and 115 (one hundred and fifteen)
# contains 20 letters. The use of "and" when writing out numbers is in
# compliance with British usage.

#full disclosure: i hate this problem so im not trying to do it elegantly
total = 0

#zero (no chars), one, two, three, four, five, six, seven, eight, nine, ten, eleven,
#twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen
ones  = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8] 

#twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety
tens = [6, 6, 5, 5, 5, 7, 6, 6]

total = 0
total99 = 0

#0-19
total = total + sum(ones)

#20-99
for x in tens:
    for y in ones[0:10]:
        total = total + x + y
total99 = total

#100
total = total + 10 #one hundred

#101-199
total = total + total99 + 99*13 #one hundred and
    
#200
total = total + 10 #two hundred
    
#201-299
total = total + total99 + 99*13 #two hundred and

#300
total = total + 12 #three hundred

#301-399
total = total + total99 + 99*15 #three hundred and
    
#400
total = total + 11 #four hundred
    
#401-499
total = total + total99 + 99*14 #four hundred and
    
#500
total = total + 11 #five hundred

#501-599
total = total + total99 + 99*14 #five hundred and
    
#600
total = total + 10 #six hundred
    
#601-699
total = total + total99 + 99*13 #six hundred and

#700
total = total + 12 #seven hundred

#701-799
total = total + total99 + 99*15 #seven hundred and
    
#800
total = total + 12 #eight hundred
    
#801-899
total = total + total99 + 99*15 #eight hundred and
    
#900
total = total + 11 #nine hundred
    
#901-999
total = total + total99 + 99*14 #nine hundred and

#1000
total = total + 11 # "one thousand"

print(total)
