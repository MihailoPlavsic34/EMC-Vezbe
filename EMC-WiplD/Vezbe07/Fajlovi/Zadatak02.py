# %%
from cmath import sqrt
from traceback import print_tb
from attr import define
import math as math
import numpy as np
from numpy import mat

fmax=1.799e9
y12=11.4e-3
R=50
c0=3e8
eps0=8.85e-12
K=1/(y12*R)
mu0=4*math.pi*10**(-7)
print('K mora biti manje od:',K)

a=150e-3
b=100e-3
c=30e-3

def kmnl(m,n,l):
    return abs(sqrt((m/b)**2+(n/c)**2+(l/a)**2))

def fmnl(m,n,l):
    return abs(kmnl(m,n,l)/(2*sqrt(mu0*eps0)))

print('Minimalna rezonantna frekvencija je: ', fmnl(1, 0, 1), 'Hz')
print('Rezonantna ucestanost pri nasoj simulaciji je na ', fmax, 'Hz')
print('ft/fmax=', fmnl(1, 0, 1)/fmax, 'Jasno se vidi da su vrednosti uporedive, te kao sto je ocekivano imamo makimalnu spregu u blizini rezonantne frekvencije')
# %%



