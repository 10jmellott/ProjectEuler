"""<a href="https://projecteuler.net/problem=24" class="title-custom-link">Lexicographic permutations</a>
A permutation is an ordered arrangement of objects. For example, 3124 is one possible 
permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically 
or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:  
012   021   102   120   201   210  
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""


from utils import permutations


def main():
    """Solves this problem

    Permutes a list of string digits.  
    Returns the indexed the millionth value.

    Quite positive this could be dynamically calculated, 
    but the number of permutations is only 10! (factorial) 
    which is ~3.6 million, so not that bad

    Returns:
        Integer: Solution to this problem
    """

    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    perms = permutations(digits)

    return perms[1000000 - 1]
