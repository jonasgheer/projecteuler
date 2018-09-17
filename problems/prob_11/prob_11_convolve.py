""" Largest product in a grid """

import numpy as np
from scipy.signal import convolve2d

data = np.genfromtxt('data.txt', delimiter=' ')

right = np.array([1,1,1,1]).reshape(1,4)
down = right.reshape(4,1)
r_dig = np.eye(4, dtype=int)
l_dig = r_dig[::-1] 

r_sum = np.max(convolve2d(data, right, mode='valid'))
d_sum = np.max(convolve2d(data, down, mode='valid'))
r_dig_sum = np.max(convolve2d(data, r_dig, mode='valid'))
l_dig_sum = np.max(convolve2d(data, l_dig, mode='valid'))



print(max(r_sum, d_sum, r_dig_sum, l_dig_sum))