import numpy as np
import matplotlib.pyplot as plt
import math

x=np.linspace(0,100e-6,1000)
Cu=1.037
t1=0.407e-6
t2=68.22e-6
U=1000
Ci=1.8
Rd=2
t=20e-6
w=0.12e6

u=U*Cu*(1-np.e**(-x/t1))*np.e**(-x/t2)


i=Ci*U/Rd*math.e**(-x/t)*np.sin(w*x)
fig1=plt.figure()
plt.plot(x,i)
fig2=plt.figure()
plt.plot(x,u)
