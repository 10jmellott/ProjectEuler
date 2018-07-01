"""<a href="https://projecteuler.net/problem=5" class="title-custom-link">Smallest multiple</a>
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.  
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from utils.fibonacci import trial_division

def main():
    """Main method to run and set the parameters for this problem
    
    Returns:
        Integer: Solution to this problem
    """
    # N is the upper bound of the range
    N = 20
    minimum_factors = {}
    # For each number in the range (skipping 1 as every number is divisible by 1)
    for i in range(2, N):
        # Factor the number
        factors = trial_division(i)
        # Create a dictionary of the number of instances of the prime factor for i
        factor_dict = {}
        for factor in factors:
            if factor in factor_dict:
                factor_dict[factor] = factor_dict[factor] + 1
            else:
                factor_dict[factor] = 1
        # Compare the factor_dictionary to the minimum_factors dictionary and set values appropriately
        #   What this does is ensures that the minimum number of instances of factors is present in the output
        for factor, count in factor_dict.items():
            if factor in minimum_factors:
                minimum_factors[factor] = max(count, minimum_factors[factor])
            else:
                minimum_factors[factor] = count

    # Now that the minimum number of instances for each prime has been determined, we simply use that to
    #   generate the minimum number divisible by all values in the range
    value = 1
    for factor, count in minimum_factors.items():
        for i in range(count):
            value = value * factor

    return value