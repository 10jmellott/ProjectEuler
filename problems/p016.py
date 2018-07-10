"""<a href="https://projecteuler.net/problem=16" class="title-custom-link">Power Digit Sum</a>
2<sup>15</sup> = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.  
What is the sum of the digits of the number 2<sup>1000</sup>?
"""


def main():
    """Solves this problem

    Python makes this a joke...  
    At least the code is pretty...

    Returns:
        Integer: Solution to this problem
    """

    # 2 ^ 1000 gets calculated: 2 ** 1000
    # Turned into a string: str(~)
    # Turned into a list of chars: list(~)
    # Each char is transformed into an int: int(s) for s in ~
    # Sum operation is performed on the list of ints: sum(~)
    return sum(int(s) for s in list(str(2 ** 1000)))
