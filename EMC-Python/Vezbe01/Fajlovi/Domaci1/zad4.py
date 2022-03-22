r1=1
r30=30
E1m=0.2
C=E1m*r1**3
E30m=E1m*(r1/r30)**3

rec='zadovoljava'

if E30m< 30e-6:
    rec='zadovoljava'
else:
    rec='ne '+rec

print('Za ',  str(E1m), 'V/m na rastojanju 1m uredjaj', rec , 'vrednost je: ' ,str(E30m))

E1m=2
C=E1m*r1**3
E30m=E1m*(r1/r30)**3

if E30m< 30e-6:
    rec='zadovoljava'
else:
    rec='ne '+rec

print('Za ', str(E1m), 'V/m na rastojanju 1m uredjaj', rec , 'vrednost je: ' ,str(E30m))

