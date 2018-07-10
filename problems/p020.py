"""<a href="https://projecteuler.net/problem=20" class="title-custom-link">Factorial digit sum</a>
n! means n × (n − 1) × ... × 3 × 2 × 1  
For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,  
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.  
Find the sum of the digits in the number 100!
"""


from functools import reduce


def main():
    """Solves this problem

    Simply allow python to work its magic and do what it does well.  
    A.K.A. Lots of conversions and reduce method for factorial

    Returns:
        Integer: Solution to this problem
    """

    # Create a list of numbers 1 to 100: range(1, 101)
    # Multiply them together with reduce method: reduce(lambda x, y: x * y, ~)
    # Convert to a string: str(~)
    # Convert to a list of characters: list(~)
    # Convert to a list of integers: int(s) for s in ~
    # Sum the list of integers: sum(~)
    return sum(int(s) for s in list(str(reduce(lambda x, y: x * y, range(1, 101)))))
