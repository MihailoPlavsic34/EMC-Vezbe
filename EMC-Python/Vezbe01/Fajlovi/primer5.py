import numpy as np
import matplotlib.pyplot as plt
import math

x=np.linspace(-2,2,100)
y=np.linspace(-2,2,100)

x,y=np.meshgrid(x,y)

z=np.sin(x**2+y**2)


fig1=plt.figure()


plt.contour(x,y,z,10) #10 je broj linija izmedju min i max vrednosti
plt.colorbar()