"""Utility package: Shared Section
"""


import math


def factor(n):
    """Finds all factors of n less than n

    Args:
        n (int): Number to factor

    Returns:
        set: Collection of all factors
    """

    factors = {1}

    for f in range(2, int(math.ceil(math.sqrt(n)) + 1)):
        if n % f == 0:
            factors.add(f)
            factors.add(int(n / f))

    return factors


def permutations(values):
    """Permutes the provided list

    Args:
        values (list): List to permute values within

    Returns:
        list: List of permutations of values
    """

    if len(values) == 1:
        return values[0]
    ret = []
    i = 0
    for item in values:
        values.remove(item)
        perms = permutations(values)
        for perm in perms:
            ret.append(item + perm)
        values.insert(i, item)
        i += 1
    return ret
