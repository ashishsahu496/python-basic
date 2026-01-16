import numpy as np

def vertical_stack(*args):
    for i in args:
        if type(i) is not np.ndarray:
            raise TypeError('Argument arr must be a numpy array')

    print(np.vstack(args))

a=np.arange(10).reshape(2,-1)
print('a==',a)
b=np.repeat(1,10).reshape(2,-1)
print('b==',b)
c=np.random.random((2,5))
print('c==',c)
vertical_stack(a,b)
vertical_stack(a,b,c)