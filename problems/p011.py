"""<a href="https://projecteuler.net/problem=11" class="title-custom-link">Largest product in a grid</a>
In the 20×20 grid below, four numbers along a diagonal line have been marked in red.  
(SEE PROJECT EULER OR INPUT FOLDER FOR GRID)  
The product of these numbers is 26 × 63 × 78 × 14 = 1788696.  
What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?
"""


from functools import reduce


def test_vertical(values, N):
    h = len(values)
    w = len(values[0])

    max_i = -1
    max_j = -1
    max_product = -1

    for i in range(h - N + 1):
        for j in range(w):
            product = 1
            for k in range(N):
                product *= values[i + k][j]
            if product > max_product:
                max_product = product
                max_i = i
                max_j = j
    
    max_values = []
    for i in range(N):
        max_values.append(values[max_i + i][max_j])

    return max_values


def test_horizontal(values, N):
    h = len(values)
    w = len(values[0])

    max_i = -1
    max_j = -1
    max_product = -1

    for i in range(h):
        for j in range(w - N + 1):
            product = 1
            for k in range(N):
                product *= values[i][j + k]
            if product > max_product:
                max_product = product
                max_i = i
                max_j = j
    
    max_values = []
    for i in range(N):
        max_values.append(values[max_i][max_j + i])

    return max_values


def test_diagonal_right(values, N):
    h = len(values)
    w = len(values[0])

    max_i = -1
    max_j = -1
    max_product = -1

    for i in range(h - N + 1):
        for j in range(w - N + 1):
            product = 1
            for k in range(N):
                product *= values[i + k][j + k]
            if product > max_product:
                max_product = product
                max_i = i
                max_j = j

    max_values = []
    for i in range(N):
        max_values.append(values[max_i + i][max_j + i])

    return max_values


def test_diagonal_left(values, N):
    h = len(values)
    w = len(values[0])

    max_i = -1
    max_j = -1
    max_product = -1

    for i in range(h - N + 1):
        for j in range(N - 1, w):
            product = 1
            for k in range(N):
                product *= values[i + k][j - k]
            if product > max_product:
                max_product = product
                max_i = i
                max_j = j

    max_values = []
    for i in range(N):
        max_values.append(values[max_i + i][max_j - i])

    return max_values


def mult(x, y):
    return x * y


def main():
    """Solves the problem
    
    Returns:
        Integer: Solution to this problem
    """
    
    # Parse input
    with open('input/p011.txt') as f:
        lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n', '')
    
    values = []
    for line in lines:
        line_list = []
        values.append(line_list)
        line_values = line.split(' ')
        for v in line_values:
            line_list.append(int(v))

    # Test consecutive values
    N = 4
    vertical_max = test_vertical(values, N)
    horizontal_max = test_horizontal(values, N)
    diag_right_max = test_diagonal_right(values, N)
    diag_left_max = test_diagonal_left(values, N)

    # Compare results
    current_max_values = vertical_max
    current_max = reduce(mult, vertical_max)

    if reduce(mult, horizontal_max) > current_max:
        current_max = reduce(mult, horizontal_max)
        current_max_values = horizontal_max

    if reduce(mult, diag_right_max) > current_max:
        current_max = reduce(mult, diag_right_max)
        current_max_values = diag_right_max

    if reduce(mult, diag_left_max) > current_max:
        current_max = reduce(mult, diag_left_max)
        current_max_values = diag_left_max
    
    # Return result
    return current_max_values, current_max
