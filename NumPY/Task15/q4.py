import numpy as np
# flip the array on the both axis
a=np.random.randint(1,100,(5,4))
print(a)
print(np.flip(a,axis=[0,1]))