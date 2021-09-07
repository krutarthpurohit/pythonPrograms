# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 09:05:02 2021

@author: Krutarth Purohit

Experiment 1
Assignment 1: Generate a numpy array and find its mean, median and min value using suitable
methods.
"""

import numpy as np
a=np.array([1,2,3,6,7,11,9])
print(a)
print(type(a))
print("Mean- ",a.mean())
print("Median- ",(a.sum()/2))
print("Minimum- ",a.min())