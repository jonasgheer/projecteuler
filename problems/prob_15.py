""" Lattice paths """

import math


def south_east_lattice(x, y):
    n, k = x + y, x
    return int(math.factorial(n) / (math.factorial(k) * math.factorial(n - k)))

x, y = 20, 20

print(f'Number of rutes through a {x}x{y} grid:', south_east_lattice(x, y))
