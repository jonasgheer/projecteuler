""" Pythagorean triplet """


import math


def euclids_formula(n, m):
    if not m > n > 0:
        raise ValueError('n, m invalid')
    a, b, c = m**2 - n**2, 2*m*n, m**2 + n**2
    return a, b, c


def find_abc(match, num_iter):
    """ Find a + b + c = match """
    for n in range(1, num_iter):
        for m in range(n+1, num_iter):
            a, b, c = euclids_formula(n, m)
            if a+b+c == match:
                return a, b, c


a, b, c = find_abc(1000, 100)

print('Product abc:', a*b*c)
