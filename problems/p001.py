"""<a href="https://projecteuler.net/problem=1">Multiples of 3 and 5</a>
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.  
Find the sum of all the multiples of 3 or 5 below 1000.
"""


def is_multiple(base, multiple):
    """Determine if base is a multiple of multiple
    
    Args:
        base (Integer): Base value
        multiple (Integer): Multiple value
    
    Returns:
        Boolean: True if base is a multiple of multiple, false otherwise
    """

    if multiple == 0:
        return False
    return base % multiple == 0


def main():
    """Main method to run and set the parameters for this problem
    
    Returns:
        Integer: Solution to this problem
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
