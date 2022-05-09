# %%
import numpy as np
import matplotlib.pyplot as plt
import math

f0=1.5e8
R=50
P=-61
f=[f0]
for i in range(10):
    f.append(f[-1]+5e6)

f=np.array(f)
I = [4.4575, 4.465, 4.486, 4.534, 4.424, 4.2775, 4.0749, 3.886, 3.68, 3.535, 3.34]
I = np.array(I)
I=I/1e3
AF=20*np.log10(1/(50*I))
fig=plt.figure()

plt.plot(f,AF)
plt.savefig(
    'D:\Storage\Documents\Faks\VIII semestar\EMC\Vezbe\EMC- AWAS\Vezbe06\Fajlovi\Zadatak03\Zadatak03.png')
plt.show()
af = AF[np.where(f == 185000000.0)[0]]
E=10**( (af+10*np.log10(R*10**(-61/10)*1e-3))/20 )
print('Intenzitet elektricnog polja za P=-61dBm, f=185 MHz je:', E, 'V/m')

# %%
