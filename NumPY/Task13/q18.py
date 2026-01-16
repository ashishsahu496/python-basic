import numpy as np

arr=np.random.randint(1,1000,40).reshape(8,5)
# print(arr)
# print(arr[:,::2])
normalies=( (arr - arr.min() )/ (arr.max() -arr.min()) )

print(normalies)