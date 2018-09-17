""" Largest product in a series  """


def slice_prod(slc):
    """ Calculate product of slice """
    prod = 1
    for n in slc:
        prod *= n
    return prod


with open('data.txt') as file:
    str_data = file.read()
    data = [int(n) for n in str_data.replace('\n', '')]


slice_size = 13


max_slice_prod = slice_prod(data[:slice_size])  # Initial max

for n in range(len(data)-slice_size):
    cur_slice_prod = slice_prod(data[n:n+slice_size])
    if cur_slice_prod > max_slice_prod:
        max_slice_prod = cur_slice_prod


print('Max 13 digit product:', max_slice_prod)
