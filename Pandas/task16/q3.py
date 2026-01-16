import pandas as pd

#  Write a Pandas program to compare the elements of the two Pandas Series.

n1=pd.Series([2, 4, 6, 8, 10])
n2=pd.Series([1, 3, 5, 7, 10])

print(n1>n2)
print(n1<n2)
print(n1==n2)
