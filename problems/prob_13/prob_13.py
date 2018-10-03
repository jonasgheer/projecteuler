""" Large sum """

num_digits = 10

with open('data.txt') as f:
    data = [int(n.replace('\n', '')) for n in f.readlines()]

print(f'First {num_digits} digits:', str(sum(data))[:10])
