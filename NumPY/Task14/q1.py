import numpy as np

def nthMin(arr,n):
    num= arr[abs(arr-n).argmin()]
    print(num)

print(nthMin(np.array([50,34,25,89,45,50]),80))