import numpy as np

a=np.array([2,3,4,5,8])
b=np.array([4,2,4,2,6])

a[b>a]=b[a<b]
print(a)
