from cProfile import label
import numpy as np
import matplotlib.pyplot as plt
import math

w=1
h=1
s=w*np.power(10, np.arange(10)/3-2)
#print(s)
t=1/1000*w
#print(t)

x=s/w
Zc=[[5.648E+01, 6.181E+01, 6.965E+01,8.112E+01, 9.761E+01, 1.206E+02,
    1.514E+02, 1.907E+02, 2.386E+02, 2.942E+02],
    [3.385E+01, 3.687E+01, 4.142E+01, 4.822E+01, 5.823E+01, 7.280E+01,
    9.393E+01, 1.242E+02, 1.647E+02, 2.128E+02]]

plt.figure()
plt.semilogx(x,Zc[0], label='Er=1')
plt.semilogx(x,Zc[1], label='Er=5')
plt.title('Zc u zavisnosti od s/w - Koplanarni talasovod')
plt.xlabel('s/w')
plt.ylabel('Zc[omima]')
plt.legend()
plt.savefig('./EMC-Linpar/Vezbe04/Fajlovi/Zadatak02.png')
plt.show()

print('Krecu se od ', str(3.385E+01), ' do ', str(2.942E+02), ' oma')
