import numpy as np
import matplotlib.pyplot as plt
import math

x=np.linspace(0.1,0.6,100)
z=np.linspace(-0.25,0.25,100)

x,z=np.meshgrid(x,z)

p=1e-12
r=(x**2+z**2)**0.5
e0=8.85e-12
V=p*(z/r)/(4*math.pi*e0*r**2)


fig1=plt.figure()


plt.pcolormesh(x,z,V, shading='gouraud')
plt.colorbar()

fig2=plt.figure()


plt.contour(x,z,V,10) #10 je broj linija izmedju min i max vrednosti
plt.colorbar()