import numpy as np
import matplotlib.pyplot as plt
import math

Zc=[1.284e2, 9.069e1,  7.121e1, 5.897e1, 5.010e1,
    4.386e1, 3.905e1, 3.521e1, 3.208e1, 2.948e1]
w_l=np.linspace(1,10,10)
fig1=plt.figure(1)
plt.plot(w_l,Zc)
plt.title('Microstrip')
plt.xlabel('w/l')
plt.ylabel('Zc[omima]')
plt.savefig('Zadatak01_fig1.png')
plt.show()