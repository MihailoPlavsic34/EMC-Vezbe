import numpy as np
import matplotlib.pyplot as plt
import math
from math import e
import matplotlib as mpl
import matplotlib.animation as ani


I=1
l=3e-3
f=3e9
c=3e8
B=2*math.pi/(c/f)
r=np.linspace(10e-2, 30e-2, 19)
teta=np.linspace(0, math.pi,19)
teta,r=np.meshgrid(teta,r)
fi=0
t=0
mi=1.3e-6
epsilon=8.85e-12
e=math.e
T=1/f
N=120
dt=T/N
iteracije=200000000000

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

E=(Ex**2+Ez**2)**0.5

fig1, ax=plt.subplots()
ax.set(title='E vektor', xlim=[0,0.3], ylim=[-0.3,0.3])
polje=ax.quiver(x,z,Ex,Ez,E, cmap='jet')
plt.show(block=False)

for i in range(iteracije):

    t=i*dt
    
    plt.pause(dt)
    
    Er=np.abs(Er_c)*2**0.5*np.cos(2*math.pi*f*t+np.angle(Er_c))
    Eo=np.abs(Eo_c)*2**0.5*np.cos(2*math.pi*f*t+np.angle(Eo_c))
    
    Ex=Er*np.sin(teta)+Eo*np.cos(teta)
    Ez=Er*np.cos(teta)-Eo*np.sin(teta)
    E=(Ex**2+Ez**2)**0.5

    
    ax.clear()
    ax.set(title='E vektor', xlim=[0,0.3], ylim=[-0.3,0.3])
    ax.quiver(x,z,Ex,Ez,E, cmap='jet')
 
    
 
# t=0
  
# fig2, ax=plt.subplots()
# plt.show(block=False)

# Er=np.abs(Er_c)*2**0.5*np.cos(2*math.pi*f*t+np.angle(Er_c))
# Eo=np.abs(Eo_c)*2**0.5*np.cos(2*math.pi*f*t+np.angle(Eo_c))

# Ex=Er*np.sin(teta)+Eo*np.cos(teta)
# Ez=Er*np.cos(teta)-Eo*np.sin(teta)
# E=(Ex**2+Ez**2)**0.5

# ax.set(title='E vektor', xlim=[0,0.3], ylim=[-0.3,0.3])
# plt.pcolormesh(x,z,E, shading='gouraud',cmap='jet')
# plt.show(block=False)

# for i in range(iteracije):

#     t=i*dt
    
    
#     plt.pause(dt)
    
#     Er=np.abs(Er_c)*2**0.5*np.cos(2*math.pi*f*t+np.angle(Er_c))
#     Eo=np.abs(Eo_c)*2**0.5*np.cos(2*math.pi*f*t+np.angle(Eo_c))
    
#     Ex=Er*np.sin(teta)+Eo*np.cos(teta)
#     Ez=Er*np.cos(teta)-Eo*np.sin(teta)
#     E=(Ex**2+Ez**2)**0.5
    
        
#     ax.clear()
#     ax.set(title='E int', xlim=[0,0.3], ylim=[-0.3,0.3])
#     plt.pcolormesh(x,z,E, shading='gouraud',cmap='jet')
    


# t=0
  

# teta=math.pi/2
# fi=np.linspace(0, 2*math.pi, 37)
# r=np.linspace(10e-2, 30e-2, 19)
# r,fi=np.meshgrid(r,fi)

# Hr=0
# Hf_c=I*l*np.sin(teta)/(4*math.pi)*(1/r**2+ 1j*B/r)*e**(-1j*B*r)
# Hf=np.abs(Hf_c)*2**0.5*np.cos(2*math.pi*f*t+np.angle(Hf_c))

# x=r*np.cos(fi)
# y=r*np.sin(fi)
# z=0

# Hx=Hf*np.cos(fi)
# Hy=-Hf*np.sin(fi)
# Hz=0
# H=(Hx**2+Hy**2)**0.5
# fig3, ax=plt.subplots()
# ax.set(title='H vektor', xlim=[0,0.3], ylim=[-0.3,0.3])
# ax.quiver(x,y,Hx,Hy,H,cmap='jet')
# plt.show(block=False)

# for i in range(iteracije):

#     t=i*dt
    
    
#     Hf=np.abs(Hf_c)*2**0.5*np.cos(2*math.pi*f*t+np.angle(Hf_c))
    
#     Hy=Hf*np.cos(fi)
#     Hx=-Hf*np.sin(fi)
#     H=(Hx**2+Hy**2)**0.5

#     plt.pause(dt)
#     ax.clear()
#     ax.set(title='H vektor', xlim=[-0.3,0.3], ylim=[-0.3,0.3])
#     ax.quiver(x,y,Hx,Hy,H,cmap='jet')
    
    

# t=0
  

# teta=math.pi/2
# fi=np.linspace(0, 2*math.pi, 37)
# r=np.linspace(10e-2, 30e-2, 19)
# r,fi=np.meshgrid(r,fi)

# Hr=0
# Hf_c=I*l*np.sin(teta)/(4*math.pi)*(1/r**2+ 1j*B/r)*e**(-1j*B*r)
# Hf=np.abs(Hf_c)*2**0.5*np.cos(2*math.pi*f*t+np.angle(Hf_c))

# x=r*np.cos(fi)
# y=r*np.sin(fi)
# z=0

# Hy=Hf*np.cos(fi)
# Hx=-Hf*np.sin(fi)
# Hz=0
# H=(Hx**2+Hy**2)**0.5
# fig3, ax=plt.subplots()
# ax.set(title='H vektor', xlim=[0,0.3], ylim=[-0.3,0.3])
# plt.pcolormesh(x,y,(Hx**2+Hy**2)**0.5, shading='gouraud',cmap='jet')
# plt.show(block=False)

# for i in range(iteracije):

#     t=i*dt
    
    
#     Hf=np.abs(Hf_c)*2**0.5*np.cos(2*math.pi*f*t+np.angle(Hf_c))
    
#     Hx=Hf*np.cos(fi)
#     Hy=-Hf*np.sin(fi)
#     H=(Hx**2+Hy**2)**0.5

#     plt.pause(dt)
#     ax.clear()
#     ax.set(title='H int', xlim=[-0.3,0.3], ylim=[-0.3,0.3])
#     plt.pcolormesh(x,y,(Hx**2+Hy**2)**0.5, shading='gouraud',cmap='jet')
