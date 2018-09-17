""" Highly divisible triangular number """


def gen_tri_num():
    """ Generate triangular numbers """
    num, floor = 1, 1
    while True:
        yield num
        floor += 1
        num += floor


def trial_division(n):
    """ Find divisors for number """
    a = []
    f = 2
    while n > 1:
        if n % f == 0:
            a.append(f)
            n /= f
        else:
            f += 1
    return a


def num_of_divisors(n):
    p_divisors = trial_division(n)
    unique = set(p_divisors)
    result = 1
    for n in unique:
        c = p_divisors.count(n)
        result *= c+1
    return result


divisors_over = 500  # number of divisors to surpass


tria_gen = gen_tri_num()
while True:
    tri_num = next(tria_gen)
    divisors = num_of_divisors(tri_num)
    if divisors > divisors_over:
        break

print(f'First triangle number with over {divisors_over} divisors:', tri_num)
