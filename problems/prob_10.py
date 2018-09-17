""" Summation of primes """


import math


def is_prime(number):
    n = 2
    while n <= math.sqrt(number):
        if number % n == 0:
            return False
        n += 1
    return True


primes = [n for n in range(2, 2_000_000) if is_prime(n)]

print('Sum of primes:', sum(primes))
