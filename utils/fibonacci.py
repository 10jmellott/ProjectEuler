"""Fibonacci's Algorithms
"""


def trial_division(n):
    """[Trial Division](https://en.wikipedia.org/wiki/Trial_division)

    Arguments:
        n (Integer): Number to factor

    Returns:
        Array: List of factors of n
    """
    a = []
    while n % 2 == 0:
        a.append(2)
        n /= 2
    f = 3
    while f * f <= n:
        if (n % f == 0):
            a.append(f)
            n /= f
        else:
            f += 2
    if n > 1:
        a.append(n)
    # Only odd number is possible
    return a


def factors_to_dictionary(factors):
    """Transforms a list of factors into a dictionary

    Args:
        factors (list): List of factors

    Returns:
        dict: Dictionary of factors to count
    """

    factor_dict = {}
    for factor in factors:
        if factor in factor_dict:
            factor_dict[factor] = factor_dict[factor] + 1
        else:
            factor_dict[factor] = 1
    return factor_dict


def fib_basic(n):
    """Simple fibonacci sequence implementation

    Arguments:
        n (Integer): Index of the fibonacci number

    Returns:
        Integer: Value of the fibonacci sequence at the provided index
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_basic(n - 1) + fib_basic(n - 2)


def fib(n):
    """Optimized fibonacci sequence implementation utilizing memoization

    Implemented as recursion. Use fib_loop for large n.

    Arguments:
        n (Integer): Index of the fibonacci number

    Returns:
        Integer: Value of the fibonacci sequence at the provided index
    """
    return fib_memo(n, {0: 0, 1: 1})


def fib_memo(n, memoization):
    """Recursive fibonacci sequence implementation utilizing memoization

    Args:
        n (Integer): Index of the fibonacci number
        memoization (Dictionary): Non-Null dictionary with prior memoized values

    Returns:
        Integer: Value of the fibonacci sequence at the provided index
    """

    if n == 0:
        return 0
    if n == 1:
        return 1
    if n in memoization:
        return memoization[n]
    memoization[n] = fib_memo(n - 1, memoization) + \
        fib_memo(n - 2, memoization)
    return memoization[n]


def fib_loop(n):
    """Optimized fibonacci sequence implementation utilizing memoization.

    Implemented as a loop. Use for large n.

    Arguments:
        n (Integer): Index of the fibonacci number

    Returns:
        Integer: Value of the fibonacci sequence at the provided index
    """

    return fib_memo_loop(n, {})


def fib_memo_loop(n, memo):
    """Looping recursive fibonacci sequence implementation utilizing memoization.

    Use for large n.

    Args:
        n (Integer): Index of the fibonacci number
        memoization (Dictionary): Non-Null dictionary with prior memoized values

    Returns:
        Integer: Value of the fibonacci sequence at the provided index
    """

    if n in memo:
        return memo[n]

    memo[0] = 0
    memo[1] = 1

    to_determine = [n]
    j = n
    while len(to_determine) > 0:
        j = to_determine.pop()
        if j - 1 in memo and j - 2 in memo:
            memo[j] = memo[j - 1] + memo[j - 2]
        else:
            to_determine.append(j)
            to_determine.append(j - 1)
            to_determine.append(j - 2)

    return memo[n]
