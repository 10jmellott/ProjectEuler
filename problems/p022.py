"""<a href="https://projecteuler.net/problem=22" class="title-custom-link">Names scores</a>
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing 
over five-thousand first names, begin by sorting it into alphabetical order. Then working 
out the alphabetical value for each name, multiply this value by its alphabetical position 
in the list to obtain a name score.  
For example, when the list is sorted into alphabetical order, COLIN, which is worth 
3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score 
of 938 × 53 = 49714.  
What is the total of all the name scores in the file?
"""

def score(name):
    v = 0
    init_value = ord('A') - 1
    chars = list(name)
    for c in chars:
        v += ord(c) - init_value
    return v


def main():
    """Solves this problem


    Returns:
        Integer: Solution to this problem
    """

    with open('input/p022.txt') as f:
        text = f.read(-1)

    names = text.split(',')
    for i in range(len(names)):
        names[i] = names[i].replace('"', '')
    names.sort()

    N = len(names)
    value = 0
    for i in range(N):
        value += score(names[i]) * (i + 1)
    return value