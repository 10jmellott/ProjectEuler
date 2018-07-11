"""<a href="https://projecteuler.net/problem=25" class="title-custom-link">1000-digit Fibonacci number</a>
The Fibonacci sequence is defined by the recurrence relation:  
    F<sub>n</sub> = F<sub>n−1</sub> + F<sub>n−2</sub>, where F<sub>1</sub> = 1 and F<sub>2</sub> = 1.  
Hence the first 12 terms will be:  
    F<sub>1</sub> = 1  
    F<sub>2</sub> = 1  
    F<sub>3</sub> = 2  
    F<sub>4</sub> = 3  
    F<sub>5</sub> = 5  
    F<sub>6</sub> = 8  
    F<sub>7</sub> = 13  
    F<sub>8</sub> = 21  
    F<sub>9</sub> = 34  
    F<sub>10</sub> = 55  
    F<sub>11</sub> = 89  
    F<sub>12</sub> = 144  
The 12th term, F<sub>12</sub>, is the first term to contain three digits.  
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""


from utils.fibonacci import fib_memo_loop


def main():
    """Solves this problem

    Keeping a list of memoized values I increment (starting arbitrarily from 1000) and continue
    to calculate the fibonacci values until the length of the str number is > 999.  

    This required utilization of a looped fibonacci method as the 
    indices exceed python's recursion limits.

    Returns:
        Integer: Solution to this problem
    """

    memo = {}
    i = 1000
    while len(str(fib_memo_loop(i, memo))) < 1000:
        i += 1
    return i
