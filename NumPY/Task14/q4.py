import numpy as np
# Your are given an array which is havig some nan value.
# You job is to fill those nan values with most common element in the array.

arr=np.array([[1,2,np.nan],[4,2,6],[np.nan,np.nan,5]])
print(arr)
d={}
for i in arr.flatten():
    if i in d:
        d[i]+=1
    else:
        d[i]=1
# print(d)
arr[np.isnan(arr)]=sorted(d.items(),key=lambda x:x[1])[-1][0]
print(arr)