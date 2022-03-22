import numpy as np
import matplotlib.pyplot as plt
import math

x=np.linspace(-2,2,100)
y=np.linspace(-2,2,100)

x,y=np.meshgrid(x,y)

z=np.sin(x**2+y**2)


fig1=plt.figure()

fig_surf=fig1.add_subplot(projection='3d')
h=fig_surf.plot_surface(x,y,z, cmap='jet')
fig_surf.set_xlabel('x')
fig_surf.set_ylabel('y')
fig_surf.set_zlabel('z')

plt.colorbar(h, location='left')
plt.show()