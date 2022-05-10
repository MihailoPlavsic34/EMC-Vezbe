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
mu0=4*math.pi*10**(-7)


a=400e-3
b=300e-3
c=200e-3

def kmnl(m,n,l):
    return abs(sqrt((m/b)**2+(n/c)**2+(l/a)**2))

def fmnl(m,n,l):
    return abs(kmnl(m,n,l)/(2*sqrt(mu0*eps0)))

print('Minimalna rezonantna frekvencija je: ', fmnl(1, 0, 1), 'Hz')

Eeff=(1**2+1**2)**0.5
Emax=5
print('Efektivna vrednost elektricnog polja van kucista je: ', Eeff, 'Odnos je: ', Emax/Eeff)
# %%
