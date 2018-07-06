"""<a href="https://projecteuler.net/problem=7" class="title-custom-link">10001st prime</a>
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.  
What is the 10 001st prime number?
"""

from utils.eratosthenes import sieve

def main():
    """Solves the problem

    Continues to calculate all primes below a threshold until the 
    number of primes is more than the required index.

    Utilizes the Sieve of Eratosthenes
    
    Returns:
        Integer: Solution to this problem
    """

    index = 10001
    X = index
    primes = sieve(X)
    while len(primes) < index:
        X *= 2
        primes = sieve(X)        
    return primes[index]