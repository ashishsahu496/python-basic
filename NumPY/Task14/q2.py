import numpy as np

a=np.array([1,2,3,4,5,6,15,34,54,30])
a[ (a%3==0) | (a%5==0)]=0
print(a)