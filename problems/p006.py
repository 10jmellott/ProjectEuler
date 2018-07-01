"""<a href="https://projecteuler.net/problem=6" class="title-custom-link">Sum square difference</a>
The sum of the squares of the first ten natural numbers is,  
1<sup>2</sup> + 2<sup>2</sup> + ... + 10<sup>2</sup> = 385  
The square of the sum of the first ten natural numbers is,  
(1 + 2 + ... + 10)<sup>2</sup> = 55<sup>2</sup> = 3025  
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.  
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

from utils.oeis import square_pyramidal_numbers
from utils.oeis import triangular_numbers

def main():
    """Main method to run and set the parameters for this problem
    
    Returns:
        Integer: Solution to this problem
    """
    
    # Doing the first 7 or so values for the sum of squares and plugging them in to OEIS database
    #   describes the sum of squares as the series of square pyramidal numbers (A000330)    
    N = 100
    square_pyramid = square_pyramidal_numbers(N)
    sequence_sum = triangular_numbers(N)
    sequence_sum_square = sequence_sum * sequence_sum
    return sequence_sum_square - square_pyramid