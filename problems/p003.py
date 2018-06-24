"""<a href="https://projecteuler.net/problem=3" class="title-custom-link">Largest prime factor</a>
The prime factors of 13195 are 5, 7, 13 and 29.  
What is the largest prime factor of the number 600851475143 ?
"""


import math
import utils.eratosthenes


def main():
    """Main method to run and set the parameters for this problem
    
    Returns:
        Integer: Solution to this problem
    """
    N = 600851475143
    # Prime factors of a number cannot be larger than the square root of a number
    n = int(math.sqrt(N) + 1)
    # Creates a list of primes and reverses them to go from largest to smallest
    primes = reversed(utils.eratosthenes.sieve(n))
    # Loop through the primes to find the first prime factor of N
    for p in primes:
        if N % p == 0:
            return p
    # N is prime
    return 1