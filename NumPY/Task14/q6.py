
# Given two arrays, X and Y, construct the Cauchy matrix C.
# Cij =1/(xi - yj)
import numpy as np
from numpy import broadcast

x = np.array([1,2,3,4]).reshape((-1, 1))
y = np.array([5,6,7])
# print(x)
# print(y)
print(np.broadcast_to(x, (4,3)))
print(np.broadcast_to(y, (4,3)))
z= 1 / (x-y)
print(z)