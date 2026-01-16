import numpy as np

# You are given an arrays. You have to limit this array's elements between 100 to 200.
# arr∈[100,700] . So replace those values accordingly with the minimum and maximum value.
# Then sort the array and perform the cumulative sum of that array.

a=np.random.randint(0,300,50)
# print(a)
limit=[np.cumsum(np.sort(np.clip(a,100,200)))]
print(limit)