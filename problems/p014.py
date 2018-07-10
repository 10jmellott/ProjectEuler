"""<a href="https://projecteuler.net/problem=14" class="title-custom-link">Longest Collatz sequence</a>
The following iterative sequence is defined for the set of positive integers:  
n → n/2 (n is even)  
n → 3n + 1 (n is odd)  
Using the rule above and starting with 13, we generate the following sequence:  
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1  
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.  
Which starting number, under one million, produces the longest chain?  
NOTE: Once the chain starts the terms are allowed to go above one million.
"""


from utils.oeis import collatz


def memoized_collatz_chain(n, chains):
    """Determines the length of the sequence until 1 using n as a base
    
    Args:
        n (Integer): Value to start the collatz sequence from
        chains (Dict): Dictionary containing previously computed chains
    
    Returns:
        Integer: Number of values in the chain until 1 for n
    """

    if n <= 1:
        return 1
    if n in chains:
        return chains[n]
    
    chains[n] = memoized_collatz_chain(collatz(n), chains) + 1
    
    return chains[n]


def main():
    """Solves this problem

    Utilizes memoization of the results of the collatz chains and 
    calculated for each value under 1000000

    Returns:
        Integer: Solution to this problem
    """

    collatz_chains = {}

    max_chain = 0
    max_n = 0

    for n in range(2, 1000000):
        chain = memoized_collatz_chain(n, collatz_chains)
        if chain > max_chain:
            max_chain = chain
            max_n = n

    return max_n, max_chain
