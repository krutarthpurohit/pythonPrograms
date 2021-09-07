# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 11:07:05 2021

@author: Krutarth Purohit

Experiment 4
Modification 2: To plot an impedance of series RLC circuit with varies input frequencies.

"""

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
R=200
C=15*10**-6
L=230*10**-3
f=np.arange(50.69,150.69,1)
temp=[]

for i in range(len(f)):
    XL=2*sp.pi*f[i]*L
    XC=1/(2*sp.pi*f[i]*C)
    Z=np.sqrt(R*R+(XL-XC)*(XL-XC))
    temp.append(Z)
    
plt.plot(f,temp);
plt.title("RLC Impedance")
plt.xlabel("Frequency")
plt.ylabel("Impedance")
plt.show()
f0=1/(2*sp.pi*np.sqrt(L*C))
print("Resonance Frequency = ",f0)
