# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 11:50:11 2021

@author: Krutarth Purohit
Experiment 6
(1) Node Voltage Analysis: KCL (Modification)
"""

from numpy import array,mat, transpose, zeros,identity,eye,divide
from numpy.linalg import inv,det,eig,matrix_rank

R=mat([[(1/7+1/2),(-2)] , [(-2),(1/2+1)]])
I=mat([[3],[-2]])

V=inv(R)*I

print(V)