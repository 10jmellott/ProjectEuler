"""Eratosthenes' Algorithms
"""


def sieve(n):
    """[Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) - Finds prime numbers
    
    Args:
        n (Integer): Maximum value to look for primes under
    
    Returns:
        Integer Array: Array of all primes less than n
    """
    integers = []
    for x in range(n):
        integers.append(True)
    prime_selected = True
    p = 2
    while p * p < n and prime_selected:
        prime_selected = False
        for x in range(p + p, n, p):
            integers[x] = False
        for x in range(p + 1, n):
            if integers[x]:
                p = x;
                prime_selected = True
                break;
    primes = []
    for x in range(2, n):
        if integers[x]:
            primes.append(x)
    return primes
