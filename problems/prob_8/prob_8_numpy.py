""" Largest product in a series (numpy) """


def slice_prod(slc):
    """ Calculate product of slice """
    prod = 1
    for n in slc:
        prod *= n
    return prod


with open('data.txt') as file:
    str_data = file.read()
    data = [int(n) for n in str_data.replace('\n', '')]


max_slice_prod = slice_prod(data[:13])  # Initial max

for n in range(len(data)-13):
    cur_slice_prod = slice_prod(data[n:n+13])
    if cur_slice_prod > max_slice_prod:
        max_slice_prod = cur_slice_prod


print('Max 13 digit product:', max_slice_prod)
