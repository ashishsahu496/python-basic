import numpy as np

#  Get row numbers of NumPy array having element larger than X.

arr=np.array([[1,2,3,4,5],
      [10,-3,30,4,5],
      [3,2,5,-4,5],
      [9,7,3,6,5]] )
x=20
print([np.where(np.any(arr>x,axis=0))])