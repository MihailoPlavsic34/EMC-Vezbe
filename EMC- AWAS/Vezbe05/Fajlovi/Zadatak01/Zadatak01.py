import math
# %%
f=1e9
c=3e8
lambda_=c/f
h=lambda_/30/2
r=h/50
s1 = math.log10(1.58/0.6)/math.log10(14e-3/10e-3)
s2 = math.log10(168/140)/math.log10(6/5)
print('Za d=(10,30)mm polje opada sa stepenom: ', s1, 'Za d=(5,10)m polje opada sa stepenom: ', s2)
