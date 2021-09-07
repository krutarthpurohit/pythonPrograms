# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 11:55:16 2021

@author: Krutarth Purohit
Experiment 6
(2) Mesh Current Analysis: KVL (Modification)
"""

from numpy import array,mat, transpose, zeros,identity,eye,divide
from numpy.linalg import inv,det,eig,matrix_rank

R=mat([[(10+3.3),(-3.3)] , [(-3.3),(3.3+2.2)]])
V=mat([[15],[-9]])

I=inv(R)*V

print(I)