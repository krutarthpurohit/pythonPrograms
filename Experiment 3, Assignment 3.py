# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 09:32:31 2021

@author: Krutarth Purohit

Experiment 3
Assignment 3: Using for loop sort the given matrix in descending order. A = [10,19,38,43,1,0]
"""

A = [10,19,38,43,1,0]

for m in range(0,len(A)):
    for n in range(m,len(A)):
        if A[m]<A[n]:
            temp=A[m]
            A[m]=A[n]
            A[n]=temp
print(A)




""" 
Same program with different method.

@authr: Hardip Shah

x=[10,15,8,25,0,1]
j=0

for i in x:
    print(i)
    j+=1
    for k in range(j,6):
        if i<=x[k]:
            temp=x[j-1]
            x[j-1]=x[k]
            x[k]=temp
print(x)
"""
    