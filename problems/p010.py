"""<a href="https://projecteuler.net/problem=10" class="title-custom-link">Summation of Primes</a>
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.  
Find the sum of all the primes below two million.
"""

from utils.eratosthenes import sieve

def main():
    """Solves this problem
    
    Utilizes the Sieve of Eratosthenes and the python sum function.
    This was a simple one...

    Returns:
        Integer: Solution to this problem
    """
    
    N = 2000000
    primes = sieve(N)
    return sum(primes)
    

