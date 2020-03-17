# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 20:32:20 2020

@author: Aiva
"""

import numpy as np
matrix1=np.eye(4)
matrix2=np.ones((4,5,3,8))

print(matrix1.ndim,"\n")
print(matrix1.shape,"\n")
print(matrix1.size,"\n")

print("For matrix 2:\n")

print(matrix2.ndim,"\n")
print(matrix2.shape,"\n")
print(matrix2.size,"\n")

print("Printing size in bytes\n")

print("For each element matrix1: ",matrix1.itemsize,"\n")
print("For the whole matrix: ",matrix1.nbytes,"\n")