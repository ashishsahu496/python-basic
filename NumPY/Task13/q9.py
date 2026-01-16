import numpy as np

a=input("enter the number : ").strip().split()
print(a)
b=np.array(a[::-1],dtype=np.float32)
print(b)
print(type(b))