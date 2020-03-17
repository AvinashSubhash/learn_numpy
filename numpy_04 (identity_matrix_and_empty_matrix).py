# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 10:55:44 2020

@author: Aiva
"""

import numpy as np
matrix1=np.eye(3)
matrix2=np.eye(3)

for i in range(0,3):
    for j in range(0,3):
        matrix1[i][j]+=matrix2[i][j]
        print(matrix1[i][j])
    print("\n")
    
matrix3=np.empty((3,3))
for i in matrix3:
    print(i)
    