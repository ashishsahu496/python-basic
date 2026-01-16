import numpy as np
# Find unique arrays from a 2D array column wise and row wise.
arr = np.array([[1,2,3,3,1,1],
                [0,9,1,2,8,8],
                [1,2,3,8,8,8],
                [1,2,3,3,1,1]])

print(np.unique(arr,axis=0))
print(np.unique(arr,axis=1))