import numpy as np
a,b=map(int,input("Enter the two number : ").split())
# print(a,b)
x=np.random.random((a,b))
print(x)
print("mean of " ,x/np.mean(x))

