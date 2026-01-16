import numpy as np

def nthMax(arr,n):
    if  n>len(arr):
        raise IndexError("way out of limit")
    arr.sort()
    return arr[-n]

print(nthMax(np.array([12,34,40,7,1,0]),3))