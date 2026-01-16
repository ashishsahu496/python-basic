import numpy as np

#  You are given a array ( arr∈[0,1] ). First you have round off the elements upto 3 decimal places and compare that
# 0th percentile == minimum value of the array
# 100th percentile == maximum value of the array
# also find the difference betwen 51th percenile and 50th percentile values

a=np.random.random(100)
# print(a)
a=np.around(a ,decimals=3)
# print(a)
print("0th percentile == minimum value of the array ",(np.percentile(a,0) == a.min()))
print("100th percentile == minimum value of the array ",(np.percentile(a,100) == a.max()))
print(" 50th and 51th percentile == minimum value of the array ",(np.percentile(a,51) - np.percentile(a,50)))