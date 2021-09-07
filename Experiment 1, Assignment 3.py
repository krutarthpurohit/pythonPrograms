# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 09:10:49 2021

@author: Krutarth Purohit

Experiment 1
Assignment 3: Write a Python function to print factorial of value 7.
"""

def sum1(n):
    if n==0:
        return 1;
    else:
        return n*sum1(n-1);
    
n=7
total=sum1(n)
print("Factorial=", total)