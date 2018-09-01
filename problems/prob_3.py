""" Largest prime factor """

import math

def lpf(number):
    """ Return largest prime factor (lpf) of a number """
    factors = []
    n = 1
    while n < math.sqrt(number):
        if number % n == 0:
            if is_prime(n):
                factors.append(n)
        n += 1
    return max(factors)

def is_prime(n):
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True

print('lpf:', lpf(600_851_475_143))
