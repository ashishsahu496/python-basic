import numpy as np

a=np.random.randint(1,20,(10,2))
# print(a)
point=np.array([2,3])
print(point)
z=np.sqrt(np.sum((a-point)**2,axis=1)).astype(int)
print(z)