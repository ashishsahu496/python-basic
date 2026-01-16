import numpy as np
#
# a=np.random.random(20).reshape(4,5)
# print(a)
# print('*'*90)
# print(a[1:-1,1:-1])

def borderArray(a,b):
    x=np.ones((a,b))
    x[1:-1,1:-1]=0
    return x

print(borderArray(4,5))
