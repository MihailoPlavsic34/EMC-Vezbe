import numpy as np
import matplotlib.pyplot as plt
import math

x=np.linspace(-2,2,10)
y=np.linspace(-2,2,10)

x,y=np.meshgrid(x,y)

z=np.sin(x**2+y**2)


fig1=plt.figure()


plt.pcolormesh(x,y,z, shading='gouraud') #ono gouraud je da malko usrednji on
plt.colorbar()