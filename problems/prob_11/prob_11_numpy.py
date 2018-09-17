""" Largest product in a grid """ 


import numpy as np


data = np.genfromtxt('data.txt', delimiter=' ')
assert data.shape == (20,20)


max_prod = 0
for r in range(data.shape[0] - 3):
    for c in range(data.shape[1] - 3):
        hor = np.prod(data[r, c:c+4])
        ver = np.prod(data[r:r+4, c])
        dia1 = np.prod(np.diagonal(data[r:r+4, c:c+4]))
        dia2 = np.prod(np.diagonal(data[r:r+4, :c+1][:,::-1]))
        max_prod = max([max_prod, hor, ver, dia1, dia2])
print(max_prod)
