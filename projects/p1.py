"""
Problem 1 - If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

def is_multiple(n, l):
    """Determines if n is a multiple of l
    
    Arguments:
        n {Integer} -- Base value
        l {Integer} -- Multiple value
    
    Returns:
        Boolean -- True if n is a multiple of l, false otherwise
    """
    if l == 0:
        return False
    return n % l == 0

def main():
    """Implementation of problem 1
    
    Returns:
        Integer -- Answer to problem 1
    """
    N = 10
    L = [3, 5]
    sum = 0
    for n in range(N):
        for l in L:
            if is_multiple(n, l):
                sum = sum + n
                break
    return sum
