"""<a href="https://projecteuler.net/problem=9" class="title-custom-link">Special Pythagorean Triplet</a>
A Pythagorean triplet is a set of three natural numbers, *a* &lt; *b* &lt; *c*, for which,  
a<sup>2</sup> + b<sup>2</sup> = c<sup>2</sup>  
For example, 3<sup>2</sup> + 4<sup>2</sup> = 9 + 16 = 25 = 5<sup>2</sup>.  
There exists exactly one Pythagorean triplet for which a + b + c = 1000.  
Find the product *abc*.
"""

def main():
    """Solves this problem
    
    Brute force solution that checks all possible values with the constrains that solve this:
    a < b < c and a + b + c = 1000
    As stated in the problem, there only exists one, so I return the first one to resolve as a triplet

    Returns:
        Integer: Solution to this problem
    """
    
    for a in range(1, 1000):
        a2 = a * a
        for b in range(a + 1, 1000):
            b2 = b * b
            c = 1000 - a - b
            if (a2 + b2) == (c * c):
                return [a, b, c], a * b * c
    
    return -1
    

