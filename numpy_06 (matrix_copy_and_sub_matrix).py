# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 21:11:44 2020

@author: Aiva
"""
import numpy as np
matrix1=np.eye(5)


        
        
print(matrix1,"\n")

matrix2=matrix1[2:5,2:5]

print(matrix2,"\n")
matrix2+=1
print(matrix1,"\n\n")
"""NOTE!!! Modifying the matrix2 will automatically modify the first (original) matrix!"""


""" For modifyig the array without changing the original array"""

matrix2=matrix1[2:5,2:5].copy()
matrix2+=1
print(matrix2)