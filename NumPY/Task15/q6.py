import numpy as np

# How to convert an array of arrays into a flat 1d array?
arr1 = np.arange(3)
arr2 = np.arange(3,7)
arr3 = np.arange(7,10)

print(np.concatenate([arr1,arr2,arr3]))