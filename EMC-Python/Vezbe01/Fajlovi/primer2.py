import numpy as np
import matplotlib.pyplot as plt
import math

x=np.linspace(0,4*math.pi,100)

y=np.cos(x)

fig1=plt.figure()
plt.plot(x,y)
plt.show()