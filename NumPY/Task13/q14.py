import statistics
import numpy as np

x=np.random.random((5,4))
# print(x)
print(x.mean(axis=1,keepdims=True))
print(x-x.mean(axis=1,keepdims=True))