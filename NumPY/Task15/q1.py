import numpy as np

#  Create a random 3x4 matrix with value between 0-100. And perform below tasks
# i. Sort this matrix. np.sort()
# ii. Sort this matrix based on values in 2nd column.
# iii. Sort this matrix based on max value in each row.
# iv. Sort based on elements value.

arr =np.random.randint(1,100,(3,4))
print(arr)
print(np.sort(arr))
print(arr[arr[:,1].argsort()])
print(np.array(sorted(arr, key=lambda x: max(x))))
print(np.sort(arr,axis=None).reshape(3,4))