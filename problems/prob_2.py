""" Even Fibonacci numbers """

def fib(limit):
    """ Return list of fib numbers up to limit """
    terms = []
    a, b = 1, 2
    while a < limit:
        terms.append(a)
        a, b = b, a+b
    return terms 

sum_even = sum([n for n in fib(4_000_000) if n % 2 == 0])
print('sum_even:', sum_even)