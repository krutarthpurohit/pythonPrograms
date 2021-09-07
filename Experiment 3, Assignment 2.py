# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 09:26:59 2021

@author: Krutarth Purohit

Experiment 3
Assignment 2: Using a nested loop find the prime numbers between 2 to 200.
"""

lower = 2
upper = 200

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)