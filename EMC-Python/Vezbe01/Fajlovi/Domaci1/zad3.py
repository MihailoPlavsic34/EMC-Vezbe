import numpy as np
import matplotlib.pyplot as plt
import math

p=1e-12
e0=8.85e-12

x=np.linspace(0.1, 0.4, 100)
z=np.linspace(-0.25, 0.25, 100)

x,z=np.meshgrid(x,z)
r=(x**2+z**2)**0.5
cos=x/r
sin=z/r

Ex=p/(4*math.pi*e0*r**3)*(3*cos*sin)
Ez=p/(4*math.pi*e0*r**3)*(3*cos**2-1)
E=(Ex**2+Ez**2)**0.5


fig1=plt.figure()
plt.quiver(x,z,Ex,Ez,E)
plt.colorbar()
plt.xlabel('x')
plt.ylabel('z')
plt.grid()
plt.title('Elektricno polje - linije')

fig2=plt.figure()
plt.xlabel('x')
plt.ylabel('z')
plt.grid()
plt.title('Elektricno polje - intenzitet')

plt.pcolormesh(x,z,E, shading='gouraud') #ono gouraud je da malko usrednji on
plt.colorbar()