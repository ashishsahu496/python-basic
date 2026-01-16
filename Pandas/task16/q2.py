import pandas as pd


# Write a Pandas program to add, subtract, multiple and divide two Pandas Series.

n1=pd.Series([1,2,3])
n2=pd.Series([4,5,6])

n3=n1 + n2
print(n3)
n4=n1-n2
print(n4)
n5=n1*n2
print(n5)
n6=n1/n2
print(n6)