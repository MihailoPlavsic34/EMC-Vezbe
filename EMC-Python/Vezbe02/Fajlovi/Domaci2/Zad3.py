import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import math
import numpy


I=1
l=3e-3
f=3e9
c=3e8
B=2*math.pi/(c/f)
min=0.01
max=10
n=100000
r=np.linspace(min, max, n)
delta=(max-min)/n
teta=math.pi/2
teta,r=np.meshgrid(teta,r)
fi=0
t=0
mi=1.3e-6
epsilon=8.85e-12
e=math.e


Er_c=I*l*np.cos(teta)/(2*math.pi)*(mi/epsilon)**0.5*(1/r**2 - 1j*1/(B*r**3))*e**(-1j*B*r)
Er=np.abs(Er_c)*2**0.5*1

Eo_c=I*l*np.sin(teta)/(4*math.pi)*(mi/epsilon)**0.5*(1/r**2+1j*(B/r-1/(B*r**3)))*e**(-1j*B*r)
Eo=np.abs(Eo_c)*2**0.5*1

#trazi se maksimalna vrednost tkd je cos postavljen na 1

Ef=0


x=r*np.sin(teta)*np.cos(fi)
y=0
z=0


Ex=Er*np.sin(teta)+Eo*np.cos(teta)
Ez=Er*np.cos(teta)-Eo*np.sin(teta)

fig1=plt.figure()
plt.title('Maksimalna vrednost elektricnog polja u zavisnosti od rastojanja')
plt.xlabel('d[m]')
plt.ylabel('E[V/m]')

E=(Ex**2+Ez**2)**0.5

plt.plot(x,E)


def slope(f,x):
    s=math.log10(f[x]/f[x+1])/math.log10(r[x+1]/r[x])
    return s

t=[]
a=0

for i in range(len(E)-1):
    if len(t)==a:
        s1=slope(E,i)
        s2=slope(E,i+1)
        dif=s1-s2
        if abs(dif)<0.01:
            t.append(s1)
    else:
        diff=t[len(t)-1]-slope(E,i)
        if abs(diff)>0.75:
            a+=1

print('Vrednosti za koje funkcija opadanja konvergira su: ')
print(t)

Emax=10
index = numpy.where(E < Emax)[0]
print('d za koju je E < Emax je:', str(r[index[0]]), 'm')
