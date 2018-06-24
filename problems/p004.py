"""<a href="https://projecteuler.net/problem=4" class="title-custom-link">Largest palindrome product</a>
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrome(n):
    """Tests if a number is a palindrome
    
    Args:
        n (Integer): Integer to test palindromomity
    
    Returns:
        Boolean: True if n is a palindrome, false otherwise
    """
    # Turn the integer into a list of characters
    chars = list(str(n))
    length = len(chars)
    # For the first half of characters and check for palindrome quality
    # Important: I know that I said half, and normally would have done that,
    #            except that the division operation AND bit shifting 
    #            is more expensive than simply checking each character (for small n)
    for i in range(length):
        if chars[i] != chars[length - i - 1]:
            return False
    return True


def main():
    """Main method to run and set the parameters for this problem
    
    Returns:
        Integer: Solution to this problem
    """
    n_max = -1
    # Loop through all pairs of three digit numbers
    for i in range(100, 999):
        for j in range(100, 999):
            n = i * j
            # Test if the product is larger than the last largest palindrome found
            if n > n_max and is_palindrome(n):
                # Set the product, and values of the largest palindrome found yet
                n_max = n
                i_max = i
                j_max = j
    # Return the product, and values for the largest palindrome
    return n_max, i_max, j_max