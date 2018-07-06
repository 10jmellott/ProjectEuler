"""<a href="https://projecteuler.net/problem=8" class="title-custom-link">Largest product in a series</a>
The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.  
(SEE PROJECT EULER OR INPUT FOLDER FOR NUMBER)  
Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
"""


def main():
    """Solves the problem
    
    Brute force approach that moves a cursor position along the number (as an array of the character digits)
    No storage of the previous product was necessary for only 13 length (& 1000 digits)

    Returns:
        Integer: Solution to this problem
    """

    N = 13
    
    with open('input/p008.txt') as f:
        lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n', '')        
    digits = list(''.join(lines))

    max_i = -1
    max_product = 1
    
    for i in range(len(digits) - N + 1):
        product = 1
        for j in range(N):
            product *= int(digits[i + j])
        if product > max_product:
            max_product = product
            max_i = i

    return max_i, digits[max_i:max_i+N], max_product