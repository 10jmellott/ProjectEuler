"""<a href="https://projecteuler.net/problem=21" class="title-custom-link">Amicable numbers</a>
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).  
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.  
For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.  
Evaluate the sum of all the amicable numbers under 10000.
"""


from utils import factor


def main():
    """Solves this problem

    Calculates the sum of the factors of all numbers under 10000.  
    Then checks each result for amicable numbers.  
    Nothing very special in terms of calculations.

    Returns:
        Integer: Solution to this problem
    """

    dn = {}
    for i in range(1, 10000):
        dn[i] = sum(factor(i))

    amicable = set()
    for k, v in dn.items():
        if k != v and v in dn and dn[v] == k:
            amicable.add(k)
    
    return sum(amicable)
