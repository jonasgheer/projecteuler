""" 10001th prime """

from math import sqrt


def is_prime(n):
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True


primes = []
n = 2
while True:
    if is_prime(n):
        primes.append(n)
    if len(primes) == 10_001:
        break
    n += 1


print('10_001th prime:', primes.pop())
