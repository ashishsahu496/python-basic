import numpy as np

# You are given a array. You have to find the minimum and maximum array element and
# remove that from the array.
arr = np.random.randint(100, 1000, 200).reshape((1, 200))
print(arr)
min_arr=np.argmin(arr)
print(min_arr)
max_arr=np.argmax(arr)
print(max_arr)
arr=np.delete(arr,min_arr,axis=1)
arr=np.delete(arr,min_arr,axis=1)
print(arr)
print(arr.max())
print(arr.min())