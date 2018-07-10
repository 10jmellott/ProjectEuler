"""<a href="https://projecteuler.net/problem=17" class="title-custom-link">Number letter counts</a>
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 
3 + 3 + 5 + 4 + 4 = 19 letters used in total.  
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
how many letters would be used?  
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 
letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out 
numbers is in compliance with British usage.
"""


def to_english(n):
    single_digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    if n <= 0:
        return None
    
    if n == 1000:
        return 'one thousand'

    if n % 100 == 0:
        r = n % 100
        return '{} hundred'.format(to_english(int((n - r) / 100)))

    if n > 100:
        r = n % 100
        return '{} and {}'.format(to_english(n - r), to_english(r))

    if n % 10 == 0:
        return tens[int(n / 10) - 1]

    if n > 20:
        r = n % 10
        return '{}-{}'.format(to_english(n - r), to_english(r))
    
    if n < 10:
        return single_digits[n - 1]
    
    if n < 20:
        return teens[n - 11]

    return None

def main():
    """Solves this problem

    Ooh, British Compliance

    Returns:
        Integer: Solution to this problem
    """

    N = 1000
    english = []
    
    for i in range(1, N + 1):
        english.append(to_english(i))

    return len(list(''.join(s.replace(' ', '').replace('-', '') for s in english)))
