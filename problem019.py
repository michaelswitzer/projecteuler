# You are given the following information, but you may prefer to do some
# research for yourself.
# 
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a
# century unless it is divisible by 400.
# 
# How many Sundays fell on the first of the month during the twentieth
# century (1 Jan 1901 to 31 Dec 2000)?

from common_funcs import answer

def is_leap(year):
    if year % 4 == 0 and not (year % 100 == 0 and not year % 400 == 0):
        return True
    return False
            
def solve():
    Sundays = 0   
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_count = (1 + sum(days_in_month)) % 7 # this is Monday 1 Jan 1900 + 365 days = 1 Jan 1901
    # day_count = 2 so 1 Jan 1901 is a Tuesday
    
    for year in range(1901,2001):
        for month in days_in_month:
            if month == 28:
                if is_leap(year):
                    day_count = (day_count + 1) % 7
            if day_count == 0:
                Sundays = Sundays + 1
            for day in range(1,month):
                day_count = (day_count + 1) % 7
    
    return Sundays

answer(solve)