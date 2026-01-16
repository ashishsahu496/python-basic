
# to find the missing data in a given array. Return a boolean matrix.
# also try to fill those missing values with 0. For that, you can use np.nan_to_num(a)
import numpy as np

a=np.array([[3, 2, np.nan, 1],
          [10, 12, 10, 9],
          [5, np.nan, 1, np.nan]])
print(np.isnan(a))
print(np.nan_to_num(a))