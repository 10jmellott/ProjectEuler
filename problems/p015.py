"""<a href="https://projecteuler.net/problem=15" class="title-custom-link">Lattice paths</a>
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.  
How many such routes are there through a 20×20 grid?
"""


def main():
    """Solves this problem

    This requires a very small bit of dynamic programming to determine 
    that a given vertex has the sum of the routes to its right and bottom values.  
    Furthermore this is then calculated by determining the edges have only 1 path 
    available and calculating the matrix from the bottom right corner in.

    Returns:
        Integer: Solution to this problem
    """

    N = 20

    vertices = [[None for j in range(N + 1)] for i in range(N + 1)]

    for i in range(N + 1):
        vertices[N][i] = 1
        vertices[i][N] = 1

    for i in range(N - 1, -1, -1):
        for j in range(N - 1, -1, -1):
            vertices[i][j] = vertices[i + 1][j] + vertices[i][j + 1]

    return vertices[0][0]
    