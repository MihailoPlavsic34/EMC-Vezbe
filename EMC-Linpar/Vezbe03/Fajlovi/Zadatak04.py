# %%
from cProfile import label
from re import L
import numpy as np
import matplotlib.pyplot as plt
import math
import pickle

import pickle

br=1

class MyClass():
    def __init__(self, param):
        self.param = param


def save_object(obj):
    try:
        with open("data.pickle%i" %br, "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)


er=[1,5]

L12 = [[2.120e-08, 4.281e-09, 8.664e-10, 3.509e-10, 4.192e-10,
        5.558e-10, 6.583e-10, 7.184e-10, 7.461e-10, 7.521e-10],
       [2.120e-08, 4.281e-09, 8.664e-10, 3.509e-10, 4.192e-10,
       5.558e-10, 6.583e-10, 7.184e-10, 7.461e-10, 7.521e-10]]
C12 = [[1.883e-12, 3.773e-13, 7.602e-14, 3.060e-14, 3.631e-14,
        4.784e-14, 5.632e-14, 6.114e-14, 6.321e-14, 6.346e-14],
       [9.415e-12, 1.887e-12, 3.801e-13, 1.530e-13, 1.816e-13,
       2.392e-13, 2.816e-13, 3.057e-13, 3.160e-13, 3.173e-13]]
s=np.linspace(1,10,len(L12[0]))

stepeniL=np.zeros(np.shape(L12))
stepeniC = np.zeros(np.shape(C12))


for i in range(0,np.shape(L12)[0]):
    plt.figure(1)
    plt.plot(s, L12[i], label='L12, Er%i' %er[i])
    plt.figure(2)
    plt.plot(s, C12[i], label='C12, Er%i' % er[i])


s1 = math.log10(L12[0][0]/L12[0][2])/math.log10(s[2]/s[0])
s2 = math.log10(L12[0][-4]/L12[0][-1])/math.log10(s[-1]/s[-4])
print('Stepeni opadanja L12 za Er1 su: ', str(s1),', ' ,str(s2))


s1 = math.log10(L12[1][0]/L12[0][2])/math.log10(s[2]/s[0])
s2 = math.log10(L12[1][-4]/L12[0][-1])/math.log10(s[-1]/s[-4])
print('Stepeni opadanja L12 za Er5 su: ', str(s1), ', ', str(s2))

s1 = math.log10(C12[0][0]/C12[0][2])/math.log10(s[2]/s[0])
s2 = math.log10(C12[0][-4]/C12[0][-1])/math.log10(s[-1]/s[-4])
print('Stepeni opadanja C12 za Er1 su: ', str(s1), ', ', str(s2))

s1 = math.log10(C12[1][0]/C12[1][2])/math.log10(s[2]/s[0])
s2 = math.log10(C12[1][-4]/C12[1][-1])/math.log10(s[-1]/s[-4])
print('Stepeni opadanja C12 za Er5 su: ', str(s1), ', ', str(s2))

obj1 = MyClass(L12)
save_object(obj1)
br+=1
obj2 = MyClass(C12)
save_object(obj2)

plt.figure(1)
plt.title('Dva stripline voda L12')
plt.xlabel('s[mm]')
plt.ylabel('L12[H/m]')
plt.savefig('Zadatak04_fig1.png')
plt.legend()

plt.figure(2)
plt.title('Dva stripline voda C12')
plt.xlabel('s[mm]')
plt.ylabel('C12[F/m]')
plt.legend()
plt.savefig('Zadatak04_fig2.png')
plt.show()


# %%
