import numpy as np
import matplotlib.pyplot as plt
import math

x=np.linspace(0,1,10)
y=np.linspace(0,1,10)

x,y=np.meshgrid(x,y)

Ex=x
Ey=y



fig1=plt.figure()
plt.quiver(x,y,Ex,Ey)

plt.xlim(-0.2, 1.2)
plt.ylim(-0.2, 1.2)

plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.title('Naslov')
plt.gca().set_aspect('equal', adjustable='box')

E=(Ex**2+Ey**2)**0.5

plt.quiver(x,y,Ex,Ey,E)

plt.colorbar()
