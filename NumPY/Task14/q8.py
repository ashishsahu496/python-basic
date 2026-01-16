import numpy as np
import matplotlib.pyplot as plt
# y=36−(x−4)2−−−−−−−−−−√+2

x=np.linspace(-2,10,100)
y=np.sqrt(36 -(x-4)**2) +2
plt.plot(x,y)
plt.title("parabola")
plt.show()