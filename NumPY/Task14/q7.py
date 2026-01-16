import numpy as np
import matplotlib.pyplot as plt

# Plot this below equation.
# y=ex−e−xex+e−x

x=np.linspace(-30,30,100)
y= (np.exp(x) - np.exp(-x))  / (np.exp(x) + np.exp(-x))
print(plt.plot(x,y))
plt.show()