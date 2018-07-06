"""<a href="https://projecteuler.net/problem=13" class="title-custom-link">Large sum</a>
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.  
(SEE PROJECT EULER OR INPUT FOLDER FOR VALUE)
"""


def main():
    """Solves this problem
    
    Pure python everyone...this problem could be cooler outside of python, 
    requiring manual addition, maybe another time

    Returns:
        Integer: Solution to this problem
    """

    with open('input/p013.txt') as f:
        lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n', '')

    value = 0
    for line in lines:
        value = value + int(line)

    return str(value)[0:10]
