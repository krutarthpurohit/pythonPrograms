# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 11:19:57 2021

@author: Krutarth Purohit

Experiment 4
Assignment 3: Calculate total impedance of circuit shown in Fig. 4.5 having R= 250 Ω, L1= 1 mH, L2= 1 mH, 
C1= 55 µF, C2= 55 µF and f= 50 Hz.
"""

import numpy as np
import scipy as sp
R=200
L1=L2=1*10**-3  
C1=C2=55*10**-6
f=60

Lt= (L1*L2)/(L1+L2)   #total inductance
Ct= C1+C2             #total capacitance

XL=2*sp.pi*f*Lt       
XC= 1/(2*sp.pi*f*Ct)

Z1=R*R+1j*(XL-XC)*(XL-XC);
Z=np.sqrt(R*R+(XL-XC)*(XL-XC));

print("Impedance = ",Z1,"Ohm")
print("Impedance = ",Z,"Ohm")