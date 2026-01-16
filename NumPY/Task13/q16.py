import numpy as np

a=np.arange(10)
a[a%2==1]=-1
print(a)
