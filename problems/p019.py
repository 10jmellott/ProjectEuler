"""<a href="https://projecteuler.net/problem=19" class="title-custom-link">Counting Sundays</a>
You are given the following information, but you may prefer to do some research for yourself.  
    1 Jan 1900 was a Monday.  
    Thirty days has September,  
    April, June and November.  
    All the rest have thirty-one,  
    Saving February alone,  
    Which has twenty-eight, rain or shine.  
    And on leap years, twenty-nine.  
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.  
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""


def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def main():
    """Solves this problem

    Incremented each day and checked from Jan 1st, 1900
    (excluded any match in 1900 until 1901 was reached)  
    Used this for testing: [https://www.onthisday.com/](https://www.onthisday.com/)

    Returns:
        Integer: Solution to this problem
    """

    # Set the arrays for days in a month
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    months_ly = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Initilized using the data provided - 0 indexed day & month - so you add one to get the actual date
    dow = 1
    day = 0
    month = 0
    year = 1900

    # Set the starting count to 0
    count = 0

    # Until we leave the 20th century
    while year < 2001:
        # determine months dataset
        m = months
        if is_leap_year(year):
            m = months_ly
        
        # Increment Count if applicable
        if day == 0 and dow == 0:
            if year > 1900:
                count += 1
        
        # Increment Day of Week
        dow += 1
        dow %= 7

        # Increment Day and cayy over into month & year
        day += 1
        if day >= m[month]:
            day = 0
            month += 1
            if month > 11:
                month = 0
                year += 1
    
    return count
