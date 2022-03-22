import numpy as np
import matplotlib.pyplot as plt
import math

def operacije(x,y):
    z=x+y
    r=x-y
    
    return np.array([z,r])

x=3e2
y=5e3

rez=operacije(x, y)
print('zbir je', rez[0], 'a razlika je ', rez[1], ' ')