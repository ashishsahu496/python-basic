import numpy as np

a=np.array([1,2,3,4,5,6,15,34,54,30])
index=[0,3,4,6,8]
a[index]*=2
# print(a)

arrr=np.array([1,2,3,4,5])
idx=[]
for i in range(len(arrr)):
    idx.extend([i] * len(arrr))
print(arrr[idx])