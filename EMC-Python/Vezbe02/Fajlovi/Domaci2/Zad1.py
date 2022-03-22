import numpy as np
import matplotlib.pyplot as plt
import math
from math import e
import matplotlib as mpl
import matplotlib.animation as ani

cmap = mpl.cm.cool

I=1
l=3e-3
f=3e9
c=3e8
B=2*math.pi/(c/f)
r=np.linspace(10e-2, 30e-2, 30)
teta=np.linspace(0, math.pi,19)
teta,r=np.meshgrid(teta,r)
fi=0
t=0
mi=1.3e-6
epsilon=8.85e-12
e=math.e


Er_c=I*l*np.cos(teta)/(2*math.pi)*(mi/epsilon)**0.5*(1/r**2 - 1j*1/(B*r**3))*e**(-1j*B*r)
Er=np.abs(Er_c)*2**0.5*np.cos(2*math.pi*f*t+np.angle(Er_c))

Eo_c=I*l*np.sin(teta)/(4*math.pi)*(mi/epsilon)**0.5*(1/r**2+1j*(B/r-1/(B*r**3)))*e**(-1j*B*r)
Eo=np.abs(Eo_c)*2**0.5*np.cos(2*math.pi*f*t+np.angle(Eo_c))

Ef=0


x=r*np.sin(teta)*np.cos(fi)
y=r*np.sin(teta)*np.sin(fi)
z=r*np.cos(teta)


Ex=Er*np.sin(teta)+Eo*np.cos(teta)
Ez=Er*np.cos(teta)-Eo*np.sin(teta)

fig1=plt.figure()
plt.title('E vektor')
plt.xlabel('x[m]')
plt.ylabel('z[m]')
E=(Ex**2+Ez**2)**0.5

plt.quiver(x,z,Ex,Ez,E, cmap='jet')
plt.colorbar()


Eff=(abs(Er_c)**2+abs(Eo_c)**2)**0.5

fig2=plt.figure()
plt.pcolormesh(x,z,Eff, shading='gouraud',cmap='jet')
plt.title('Eeff')
plt.xlabel('x[m]')
plt.ylabel('z[m]')
plt.colorbar()



fig3=plt.figure()
plt.pcolormesh(x,z,E, shading='gouraud',cmap='jet')
plt.title('Eint')
plt.xlabel('x[m]')
plt.ylabel('z[m]')
plt.colorbar()

#H vektrosi i intenzitet

teta=math.pi/2
fi=np.linspace(0, 2*math.pi, 37)
r=np.linspace(10e-2, 30e-2, 30)
r,fi=np.meshgrid(r,fi)

Hr=0
Hf_c=I*l*np.sin(teta)/(4*math.pi)*(1/r**2+ 1j*B/r)*e**(-1j*B*r)
Hf=np.abs(Hf_c)*2**0.5*np.cos(2*math.pi*f*t+np.angle(Hf_c))

x=r*np.cos(fi)
y=r*np.sin(fi)
z=0



Hx=-Hf*np.sin(fi)
Hy=Hf*np.cos(fi)
Hz=0

fig4=plt.figure()

H=(Hx**2+Hy**2)**0.5

plt.quiver(x,y,Hx,Hy,H,cmap='jet')
plt.colorbar()

plt.title('H vektor')
plt.xlabel('x[m]')
plt.ylabel('y[m]')

fig5=plt.figure()
plt.pcolormesh(x,y,(Hx**2+Hy**2)**0.5, shading='gouraud',cmap='jet')
plt.colorbar()

plt.title('H intenzitet')
plt.xlabel('x[m]')
plt.ylabel('y[m]')