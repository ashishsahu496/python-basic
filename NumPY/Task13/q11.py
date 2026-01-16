import numpy as np
from numpy.random import exponential



def softmax(arr):
    if type(arr) !=np.ndarray:
        raise TypeError('Argument arr must be a numpy array')
    elif  arr.ndim  > 1:
        raise TypeError(" require 1D array")
    exponential = np.exp(arr)
    sum=np.sum(exponential)
    return exponential/sum

print(softmax(np.array([86.03331084 ,37.7285648 , 48.64908087 ,87.16563062 ,38.40852563 ,37.20006318])))
print(np.arange(5))
