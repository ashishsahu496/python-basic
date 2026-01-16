import numpy as np

a=np.array([1,2,3])
b=np.repeat(a,3)
c=np.tile(a,3)
# print(b)
# print(c)
d=np.hstack([a,b,c])
print(d)