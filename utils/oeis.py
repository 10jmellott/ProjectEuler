"""<a href="https://oeis.org/" class="title-custom-link">The On-Line Encyclopedia of Integer Sequences</a>
This is an online database of useful sequences and some initial values to quickly 
retrieve a formula rather than coming up with one yourself.
"""


def collatz(n):
    """[Collatz Sequence](https://oeis.org/A006370)
    
    Args:
        n (Integer): Current Value of the Collatz Sequence
    
    Returns:
        Integer: Result of the next value in the Collatz Sequence following n
    """

    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1


def square_pyramidal_numbers(n):
    """[Square Pyramidal Numbers - A000330](https://oeis.org/A000330)
    
    Arguments:
        n (Integer): Index of the sequence
    
    Returns:
        Integer: Value of this sequence at the specified index
    """
    return n * (n + 1) * (2 * n + 1) / 6


def triangular_numbers(n):
    """[Triangular Numbers - A000217](https://oeis.org/A000217)
    
    Arguments:
        n (Integer): Index of the sequence
    
    Returns:
        Integer: Value of this sequence at the specified index
    """
    return n * (n + 1) / 2