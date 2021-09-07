# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 11:12:20 2021

@author: Krutarth Purohit

Experiment 4
Assignment 1: Calculate an impedance of Series RC circuit. R= 350 Ω, C= 45 µF and f= 50 Hz.
"""

import numpy as np
import scipy as sp
R=350
C=45*10**-6
f=50

XC=1/(2*sp.pi*f*C)
Z1=R*R+1j*(XC*XC)
Z=np.sqrt(R*R+XC*XC)
print("Impedance = ",Z1,"Ohm")
print("Impedance = ",Z,"Ohm")