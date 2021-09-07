# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 11:42:07 2021

@author: Krutarth Purohit
Experiment 6
(2) Mesh Current Analysis: KVL
"""

from numpy import array,mat, transpose, zeros,identity,eye,divide
from numpy.linalg import inv,det,eig,matrix_rank

R=mat([[(6+6),(-6)] , [(-6),(6+3)]])
V=mat([[12],[-3]])

I=inv(R)*V

print(I)