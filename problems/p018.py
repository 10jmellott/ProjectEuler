"""<a href="https://projecteuler.net/problem=18" class="title-custom-link">Maximum path sum I</a>
By starting at the top of the triangle below and moving to adjacent numbers on the row below, 
the maximum total from top to bottom is 23.  
3  
7 4  
2 4 6  
8 5 9 3  
That is, 3 + 7 + 4 + 9 = 23.  
Find the maximum total from top to bottom of the triangle below:  
(SEE PROJECT EULER OR INPUT FOLDER FOR VALUE)  
NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. 
However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot 
be solved by brute force, and requires a clever method! ;o)
"""


def main():
    """Solves this problem

    Note: Adjacent for my input means numbers below one level at the 
    same position or one to the right.

    Returns:
        Integer: Solution to this problem
    """

    with open('input/p018_simple.txt') as f:
        lines = f.readlines()
    
    # This is just fancy python to transform the input into an integer triangle
    split = [line.replace('\n', '').split(' ') for line in lines]
    triangle = [[int(s) for s in row] for row in split]

    # In-Place Substitution, we go from the bottom up and determine the max sum
    #   Once more this solution utilizes dynamic programming as we simply determine
    #   the maximum sum at a level where there is only one choice and use that value
    rows = len(triangle)
    for row in range(rows - 2, -1, -1):
        cols = len(triangle[row])
        for col in range(cols):
            triangle[row][col] = triangle[row][col] + \
                max(triangle[row + 1][col], triangle[row + 1][col + 1])
    
    return triangle[0][0]
