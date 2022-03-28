# %%

from cProfile import label
from re import L
import numpy as np
import matplotlib.pyplot as plt
import math

Er=[1,5]

L12 = [[9.040e-10, 4.156e-10, 2.377e-10, 1.537e-10, 1.075e-10,
        7.932e-11, 6.094e-11, 4.829e-11, 3.920e-11],
       [9.040e-10, 4.156e-10, 2.377e-10, 1.537e-10, 1.075e-10,
       7.932e-11, 6.094e-11, 4.829e-11, 3.920e-11]]
C12 = [[5.177e-14, 2.380e-14, 1.361e-14, 8.800e-15, 6.153e-15,
       4.542e-15, 3.489e-15, 2.765e-15, 2.245e-15],
       [2.728e-14, 1.256e-14, 7.212e-15, 4.675e-15, 3.281e-15,
       2.427e-15, 1.865e-15, 1.482e-15, 1.205e-15]]
s=np.linspace(20,100,len(L12[0]))

stepeniL=np.zeros(np.shape(L12))
stepeniC = np.zeros(np.shape(C12))

fig1=plt.figure(1)
#for i in range(0,len(L12[:][0])-1):
for i in range(0,np.shape(L12)[0]):
    plt.figure(1)
    plt.plot(s, L12[i], label='L12, Er=%i' %Er[i])
    plt.figure(2)
    plt.plot(s, C12[i], label='C12, Er=%i' % Er[i])


s1 = math.log10(L12[0][0]/L12[0][2])/math.log10(s[2]/s[0])
s2 = math.log10(L12[0][7]/L12[0][-1])/math.log10(s[-1]/s[7])
print('Stepeni opadanja L12 za Er=1 su: ', str(s1),', ' ,str(s2))


s1 = math.log10(L12[1][0]/L12[0][2])/math.log10(s[2]/s[0])
s2 = math.log10(L12[1][7]/L12[0][-1])/math.log10(s[-1]/s[7])
print('Stepeni opadanja L12 za Er=5 su: ', str(s1), ', ', str(s2))

s1 = math.log10(C12[0][0]/C12[0][2])/math.log10(s[2]/s[0])
s2 = math.log10(C12[0][7]/C12[0][-1])/math.log10(s[-1]/s[7])
print('Stepeni opadanja C12 za Er=1 su: ', str(s1), ', ', str(s2))

s1 = math.log10(C12[1][0]/C12[1][2])/math.log10(s[2]/s[0])
s2 = math.log10(C12[1][7]/C12[1][-1])/math.log10(s[-1]/s[7])
print('Stepeni opadanja C12 za Er=5 su: ', str(s1), ', ', str(s2))

plt.figure(1)
plt.title('Dva mikrotrakasta voda L12')
plt.xlabel('s[mm]')
plt.ylabel('L12[H/m]')
plt.savefig('Zadatak03_fig1.png')
plt.legend()

plt.figure(2)
plt.title('Dva mikrotrakasta voda C12')
plt.xlabel('s[mm]')
plt.ylabel('C12[F/m]')
plt.legend()
plt.savefig('Zadatak03_fig2.png')
plt.show()




# %%
