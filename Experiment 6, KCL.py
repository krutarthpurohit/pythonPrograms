# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 11:10:42 2021

@author: Krutarth Purohit

Experiment 6
(1) Node Voltage Analysis: KCL
"""

from numpy import array,mat, transpose, zeros,identity,eye,divide
from numpy.linalg import inv,det,eig,matrix_rank

R=mat([[(1/6+1/12),(-1/6)] , [(-1/6),(1/6+1/6)]])
I=mat([[1],[-4]])

V=inv(R)*I

print(V)