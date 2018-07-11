"""<a href="https://projecteuler.net/problem=23" class="title-custom-link">Non-abundant sums</a>
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 
28 is a perfect number.  
A number n is called deficient if the sum of its proper divisors is less than n and it is called 
abundant if this sum exceeds n.  
As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be 
written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that 
all integers greater than 28123 can be written as the sum of two abundant numbers. However, this 
upper limit cannot be reduced any further by analysis even though it is known that the greatest 
number that cannot be expressed as the sum of two abundant numbers is less than this limit.  
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""


from utils import factor


def main():
    """Solves this problem

    There are probably better solutions to this.  
    Step 1: Calculate all abundant numbers < 28124  
    Step 2: Sum ALL combinations of these and place into a SET (important)  
    Step 3: Check each number < 28124 if it is in the set above and sum the values that aren't  

    Note: This relies HEAVILY on attributes of sets to quickly index values

    Returns:
        Integer: Solution to this problem
    """

    # Step 1: Calculate all abundant numbers < 28124
    abundant = []
    for i in range(12, 28124):
        if sum(factor(i)) > i:
            abundant.append(i)
    
    # Step 2: Calculate all possible sums of the abundant numbers < 28124
    sums = set()
    for i in abundant:
        for j in abundant:
            s = i + j
            # This is faster than adding every combination - YMMV
            if s > 28123:
                break
            sums.add(s)
    
    # Step 3: Check each number if it was produced via two abundant numbers
    non_abundant = 0
    for n in range(1, 28124):
        if n not in sums:
            non_abundant += n

    return non_abundant
