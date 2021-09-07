# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 09:12:38 2021

@author: Krutarth Purohit

Experiment 2
Assignment 1:
Solve the following: 
  2x + 5y - 8z = -3
  5x - 7y + 3z = 7
  -9x + 4y + 11z = 13
"""

from numpy import array,mat, transpose, zeros,identity,eye,divide
from numpy.linalg import inv,det,eig,matrix_rank

R=mat([[2,5,-8],[5,-7,3],[-9,4,11]])
V=mat([[-3],[7],[13]])

I=inv(R)*V

print(I)