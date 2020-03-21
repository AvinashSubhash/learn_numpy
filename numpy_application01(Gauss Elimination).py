# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 20:14:35 2020

@author: Aiva
"""

import numpy as np


matrix=np.zeros((3,3))
matrix2=np.zeros((3,3))



for i in range(0,3):
    for j in range(0,3):
        print("Enter the element[",i+1,"][",j+1,"]:")
        matrix[i][j]=input()
        print(matrix[i][j],"\n")
matrix2=matrix
print(matrix2,"\n")        

        
for k in range(2):
            multiple=np.zeros(3)
            for i in range(k+1,3):
                if matrix[k][k]==0:
                    continue
                else:
                    multiple[i]=matrix[i][k]/matrix[k][k]
                
                
            for i in range(1,3):
                for j in range(3):
                    if multiple[i]==0:
                        continue
                    else:
                        matrix[i][j]=matrix[i][j]-(multiple[i]*matrix[k][j])
                    
                
                
                
print(matrix)
                
                