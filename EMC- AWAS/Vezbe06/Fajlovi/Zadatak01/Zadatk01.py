# %%
f=900e6
c=3e8
lambda_=c/f
h=lambda_/2

xmax=h*2+h/2
x=[]

for i in range(6):
    x.append(xmax -i*h)

P=[16,32,48]
I0 = [0.0778, 0.11, 0.1347]
ii=0
for i in I0:
    print('Za ', P[ii], 'W Io=', i, 'A')
    ii+=1
print('I0 je racunato preko veze P ~ Io^2, pocevsi od 1A')

E20 = [2.5, 3, 4.101]
E3 = [15, 20, 26.508]

ii=0
for i in I0:
    print('Za I0=', i, 'A, E=20V/m je zadovoljeno za: ', E20[ii], 'm; E=3V/m je zadovoljeno za: ', E3[ii], 'm')
    ii+=1

# %%
print(0.0778*(32/16)**0.5*(48/32)**0.5)

C = [-1.23E+00, 2.73E+00]
Z=(C[0]**2+C[1]**2)**0.5
print(Z)
# %%
