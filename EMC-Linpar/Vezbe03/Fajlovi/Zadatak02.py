import numpy as np
import matplotlib.pyplot as plt

Zc = [1.022E+02, 6.680E+01, 4.966E+01, 3.950E+01, 3.279E+01,
      2.801E+01, 2.444E+01, 2.168E+01, 1.947E+01, 1.767E+01]
w_l=np.linspace(1,10,len(Zc))
fig1=plt.figure(1)
plt.plot(w_l,Zc)
plt.title('Stripline')
plt.xlabel('w/l')
plt.ylabel('Zc[Omima]')
plt.savefig('Zadatak02_fig1.png')
plt.show()