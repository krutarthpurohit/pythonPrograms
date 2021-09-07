# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 11:16:40 2021

@author: Krutarth Purohit

Experiment 4
Assignment 2: Calculate an impedance of Series RL circuit. R= 350 Ω, L= 100 mH and f= 60 Hz.
"""

import numpy as np
import scipy as sp
R=350
L=100*10**-3
f=60

XL=2*sp.pi*f*L
Z1=R*R+1j*(XL*XL)
Z=np.sqrt(R*R+XL*XL)
print("Impedance = ",Z1,"Ohm")
print("Impedance = ",Z,"Ohm")