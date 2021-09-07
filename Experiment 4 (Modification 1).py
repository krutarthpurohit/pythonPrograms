# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 12:11:26 2021

@author: Krutarth Purohit

Experiment 4
Modification 1
"""
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

R=200;
C=15*10**-6
L=230*10**-3

f=np.arange(0,150,1)

temp=[]
for i in range(len(f)):
    XL=2*sp.pi*f[i]*L
    XC=1/(2*sp.pi*f[i]*C)

    Z1=R+1j*(XL-XC)
    Z=np.sqrt((R*R)+(XL-XC)**2)
    temp.append(Z)
plt.plot(f,temp)

print("Impedance = ",Z1,"Ohm")
print("Impedance = ",temp,"Ohm")