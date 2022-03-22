import numpy as np
import matplotlib.pyplot as plt
import math


l=3e-3
f=3e9
mi=1.3e-6
epsilon=8.85e-12
c=3e8
B=2*math.pi/(c/f)
teta=np.linspace(-math.pi, math.pi)
fi=np.linspace(0, 2*math.pi)
teta,fi=np.meshgrid(teta,fi)
Z=(mi/epsilon)**0.5
F=B*l/2*np.sin(teta)
Rz=20*(B*l)**2
gd1=Z/math.pi*F**2/Rz


gdz1=gd1*np.cos(teta)
gdx1=gd1*np.sin(teta)*np.cos(fi)
gdy1=gd1*np.sin(teta)*np.sin(fi)

fig1=plt.figure()

fig_surf=fig1.add_subplot(projection='3d')
scmap=plt.cm.ScalarMappable(cmap='jet')
fcolors=scmap.to_rgba(gd1)
fig_surf.set_zlim(-1.5,1.5)
fig_surf.set_title('hercov dipol')
fig_surf.set(xlabel='x[m]', ylabel='y[m]', zlabel='z[m]')
fig_surf.plot_surface(gdx1,gdy1,gdz1, facecolors=fcolors,cmap='jet')

F=np.cos(math.pi/2*np.cos(teta))/np.sin(teta)
Rz=73
gd=Z/math.pi*F**2/Rz

gdz=gd*np.cos(teta)
gdx=gd*np.sin(teta)*np.cos(fi)
gdy=gd*np.sin(teta)*np.sin(fi)

fig2=plt.figure()
fig_surf=fig2.add_subplot(projection='3d')
scmap=plt.cm.ScalarMappable(cmap='jet')
fcolors=scmap.to_rgba(gd)
fig_surf.set_zlim(-1.5,1.5)
fig_surf.set_title('Polutalasni dipol')
fig_surf.set(xlabel='x[m]', ylabel='y[m]', zlabel='z[m]')
fig_surf.plot_surface(gdx,gdy,gdz, facecolors=fcolors,cmap='jet')

print("jasno je da je glavni pravac zracenja pri teta=Pi rad, dok je fi={0,2Pi} rad. Sto se jasno vidi iz formule i posmatranjem dijagrama zracenja")
