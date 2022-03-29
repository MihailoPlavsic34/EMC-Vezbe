
# %%
import math

s1 = math.log10(2.6e-3/1.0e-3)/math.log10(55e-3/40e-3)
s2 = math.log10(360/150)/math.log10(50e-3/40e-3)
s3 = math.log10(2.5/1.2)/math.log10(10/5)
s4 = math.log10(240/120)/math.log10(10/5)
print('Hz bez provodne ravni opada kao stepen: ', s1)
print('Hz sa beskonacnom provodnom ravni opada kao stepen: ', s2)
print('na 30MHz Ey opada kao stepen: ', s3)
print('Na 10m elektricno polje je: 1.2e-6 V/m - sto zadovoljava standard')
print('na 300MHz Ey opada kao stepen: ', s4)
print('Na 10m elektricno polje je: 120e-6 V/m - sto zadovoljava standard')
print('Sa grafika se vidi da je najveci gejn (samim tim i sprega) u ravni konture')
# %%
