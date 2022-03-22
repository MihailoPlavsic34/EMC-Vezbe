from cProfile import label
from email.policy import strict
from re import L
from turtle import shape
import numpy as np
import matplotlib.pyplot as plt
import math
import pickle


class MyClass():
    def __init__(self, param):
        self.param = param


def load_object(filename):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported):", ex)


obj1 = load_object("data.pickle1")
obj2 = load_object("data.pickle2")

L12_1=obj1.param
C12_1=obj2.param


er=[1,5]

L12 = [[1.384E-09, 2.832E-10, 5.682E-11, 1.095E-11, 2.042E-12,
        4.407E-13, 9.706E-14, 4.115E-14],
       [1.384E-09, 2.832E-10, 5.682E-11, 1.095E-11, 2.042E-12,
       4.407E-13, 9.706E-14, 4.115E-14]]
C12 = [[1.051E-14, 2.148E-15, 4.296E-16, 8.459E-17, 2.165E-17,
        1.301E-17, 4.793E-18, 4.250E-18],
       [5.255E-14, 1.073E-14, 2.136E-15, 4.125E-16, 9.566E-17,
       5.291E-17, 1.292E-17, 3.066E-17]]
s=np.linspace(3,10,len(L12[0]))

stepeniL=np.zeros(np.shape(L12))
stepeniC = np.zeros(np.shape(C12))


for i in range(0,np.shape(L12)[0]):
    plt.figure(1)
    plt.plot(s, L12[i], label='L12, Er%i' %er[i])
    plt.figure(2)
    plt.plot(s, C12[i], label='C12, Er%i' % er[i])


s1 = math.log10(L12[0][0]/L12[0][2])/math.log10(s[2]/s[0])
s2 = math.log10(L12[0][-4]/L12[0][-1])/math.log10(s[-1]/s[-4])
print('Stepeni opadanja L12 za Er=1 su: ', str(s1),', ' ,str(s2))


s1 = math.log10(L12[1][0]/L12[0][2])/math.log10(s[2]/s[0])
s2 = math.log10(L12[1][-4]/L12[0][-1])/math.log10(s[-1]/s[-4])
print('Stepeni opadanja L12 za Er=5 su: ', str(s1), ', ', str(s2))

s1 = math.log10(C12[0][0]/C12[0][2])/math.log10(s[2]/s[0])
s2 = math.log10(C12[0][-4]/C12[0][-1])/math.log10(s[-1]/s[-4])
print('Stepeni opadanja C12 za Er=1 su: ', str(s1), ', ', str(s2))

s1 = math.log10(C12[1][0]/C12[1][2])/math.log10(s[2]/s[0])
s2 = math.log10(C12[1][-4]/C12[1][-1])/math.log10(s[-1]/s[-4])
print('Stepeni opadanja C12 za Er=5 su: ', str(s1), ', ', str(s2))

t_L=[]
t_C=[]

for i in range(np.shape(L12)[0]):
    for ii in range(np.shape(L12)[1]):
        t_L.append(L12[i][ii]/L12_1[i][ii+2])
        t_C.append(C12[i][ii]/C12_1[i][ii+2])

print('Vrednosti L se odnose kao: ', str(t_L[0:np.shape(L12)[1]]), ' za Er=1')


plt.figure(1)
plt.title('Stripline - 3 trake L12')
plt.xlabel('s[mm]')
plt.ylabel('L12[H/m]')
plt.savefig('Zadatak05_fig1.png')
plt.legend()

plt.figure(2)
plt.title('Stripline - 3 trake C12')
plt.xlabel('s[mm]')
plt.ylabel('C12[F/m]')
plt.legend()
plt.savefig('Zadatak05_fig2.png')
plt.show()