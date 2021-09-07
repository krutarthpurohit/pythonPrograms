# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 12:13:24 2021

@author: Krutarth Purohit

Experiment 6
Assignment 1: Applying node voltage analysis, find the value of node voltages v1 and v2 for the circuit shown 
in Fig. 6.3.
"""

from numpy import array,mat, transpose, zeros,identity,eye,divide
from numpy.linalg import inv,det,eig,matrix_rank

R=mat([[(1/2+1/4),(-1/4)] , [(1/4+1/6),(-1/4)]])
I=mat([[5],[5]])

V=inv(R)*I

print(V)