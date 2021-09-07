# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 12:32:08 2021

@author: Krutarth Purohit

Experiment 6
Assignment 2: Applying mesh current analysis, determine the currents in all three meshes for circuit shown in 
Fig. 6.4.
"""

from numpy import array,mat, transpose, zeros,identity,eye,divide
from numpy.linalg import inv,det,eig,matrix_rank

R=mat([[46,-25,-50],[-25,-6,1],[50,-1,-104]])
V=mat([[10],[0],[0]])

I=inv(R)*V

print(I)